"""Import structured JSON research data into the SQLite master database.

Data files live under ``data/<entity>/*.json`` where ``<entity>`` is one of:
authors, works, movements, periods, genres, themes, sources, relationships.

The import is idempotent: records are matched by natural keys (author full
name; work title + authorship status + composition start; unique names for
periods/movements/genres/themes/sources) and updated if present, inserted if
absent. Re-running an import never duplicates records. Relationship rows use
composite primary keys and are inserted with OR IGNORE semantics.

The relationships JSON is authoritative for every owner it names (the work,
author, period or movement on the left of a link). Before any link is
inserted, the existing rows of those owners are deleted, so a genre, theme,
movement, source, influence, attribution or edition removed from the data is
also removed from the database instead of surviving as a stale row. Owners
that no relationships file names are left untouched.

Usage:
    python scripts/import_data.py [--dry-run]

Exit code 1 if any JSON references could not be resolved.
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import Table, func, select, text  # noqa: E402

from models import (  # noqa: E402
    Author,
    Genre,
    Movement,
    Period,
    Source,
    Theme,
    Work,
    WorkAuthor,
    WorkEdition,
    author_genres,
    author_influences,
    author_movements,
    author_sources,
    author_themes,
    movement_sources,
    period_movements,
    work_genres,
    work_movements,
    work_periods,
    work_sources,
    work_themes,
    get_session,
)

DATA_ROOT = PROJECT_ROOT / "data"

JSON_LIST_FIELDS = (
    "alternative_names",
    "pseudonyms",
    "major_influences",
    "alternative_titles",
    "editions",
    "modern_translations",
    "related_works",
    "manuscript_locations",
)

warnings = []


def warn(message: str) -> None:
    warnings.append(message)
    print(f"WARNING: {message}", file=sys.stderr)


def load_json_files(entity: str):
    directory = DATA_ROOT / entity
    if not directory.is_dir():
        return []
    files = sorted(directory.glob("*.json"))
    records = []
    for path in files:
        with open(path, encoding="utf-8") as handle:
            payload = json.load(handle)
        if isinstance(payload, list):
            records.extend(payload)
        elif isinstance(payload, dict) and entity == "relationships":
            records.append(payload)
        else:
            warn(f"{path}: expected a JSON list (or relationships object)")
    return records


def serialize_json_lists(record: dict) -> dict:
    clean = dict(record)
    for field in JSON_LIST_FIELDS:
        if field in clean and not isinstance(clean[field], str):
            clean[field] = json.dumps(clean[field], ensure_ascii=False)
    return clean


# ---------------------------------------------------------------- entities

def upsert_period(session, record) -> Period:
    row = session.query(Period).filter_by(name=record["name"]).first()
    if row is None:
        row = Period(**record)
        session.add(row)
    else:
        for key, value in record.items():
            setattr(row, key, value)
    return row


def upsert_movement(session, record) -> Movement:
    row = session.query(Movement).filter_by(name=record["name"]).first()
    if row is None:
        row = Movement(**record)
        session.add(row)
    else:
        for key, value in record.items():
            setattr(row, key, value)
    return row


def upsert_genre(session, record) -> Genre:
    row = session.query(Genre).filter_by(name=record["name"]).first()
    parent = None
    if record.get("parent_genre"):
        parent = session.query(Genre).filter_by(name=record["parent_genre"]).first()
        if parent is None:
            warn(f"genre '{record['name']}': parent genre '{record['parent_genre']}' not found")
    clean = {k: v for k, v in record.items() if k != "parent_genre"}
    clean["parent_genre_id"] = parent.genre_id if parent else None
    if row is None:
        row = Genre(**clean)
        session.add(row)
    else:
        for key, value in clean.items():
            setattr(row, key, value)
    return row


def upsert_theme(session, record) -> Theme:
    row = session.query(Theme).filter_by(name=record["name"]).first()
    parent = None
    if record.get("parent_theme"):
        parent = session.query(Theme).filter_by(name=record["parent_theme"]).first()
        if parent is None:
            warn(f"theme '{record['name']}': parent theme '{record['parent_theme']}' not found")
    clean = {k: v for k, v in record.items() if k != "parent_theme"}
    clean["parent_theme_id"] = parent.theme_id if parent else None
    if row is None:
        row = Theme(**clean)
        session.add(row)
    else:
        for key, value in clean.items():
            setattr(row, key, value)
    return row


def upsert_source(session, record) -> Source:
    row = session.query(Source).filter_by(title=record["title"]).first()
    if row is None:
        row = Source(**record)
        session.add(row)
    else:
        for key, value in record.items():
            setattr(row, key, value)
    return row


def upsert_author(session, record) -> Author:
    row = session.query(Author).filter_by(full_name=record["full_name"]).first()
    clean = serialize_json_lists(record)
    if row is None:
        row = Author(**clean)
        session.add(row)
    else:
        for key, value in clean.items():
            setattr(row, key, value)
    return row


def upsert_work(session, record) -> Work:
    row = (
        session.query(Work)
        .filter_by(
            title=record["title"],
            authorship_status=record.get("authorship_status", "single"),
            composition_date_start=record.get("composition_date_start"),
        )
        .first()
    )
    clean = serialize_json_lists(record)
    if row is None:
        row = Work(**clean)
        session.add(row)
    else:
        for key, value in clean.items():
            setattr(row, key, value)
    return row


# ------------------------------------------------------------- relationships

def resolve_author(session, name):
    return session.query(Author).filter_by(full_name=name).first()


def resolve_work(session, title):
    return session.query(Work).filter_by(title=title).first()


LINK_TABLES = (
    work_genres, work_themes, work_movements, work_sources, work_periods,
    author_genres, author_movements, author_themes, author_sources,
    author_influences, period_movements, movement_sources,
)


def count_link_rows(session) -> int:
    """Total rows in every table that the relationships JSON populates."""
    tables = LINK_TABLES + (WorkAuthor.__table__, WorkEdition.__table__)
    return sum(
        session.execute(select(func.count()).select_from(table)).scalar()
        for table in tables
    )


def clear_owned_links(session, payloads) -> int:
    """Delete the existing link rows of every owner named in ``payloads``.

    Owners are resolved exactly as ``import_relationships`` resolves them
    (``resolve_work`` takes the first work with a title, the lookup dicts
    the last), so cleared rows are always the ones that are re-inserted.
    Returns the number of rows deleted.
    """
    session.flush()
    first_work, last_work = {}, {}
    for work in session.query(Work).all():
        first_work.setdefault(work.title, work.work_id)
        last_work[work.title] = work.work_id
    authors = {a.full_name: a.author_id for a in session.query(Author).all()}
    periods = {p.name: p.period_id for p in session.query(Period).all()}
    movements = {m.name: m.movement_id for m in session.query(Movement).all()}

    def by_work(lookup):
        return lambda item: [lookup.get(item["work"])]

    def by_author(item):
        return [authors.get(item["author"])]

    owners = {
        "work_authors": (WorkAuthor, "work_id", by_work(first_work)),
        "work_editions": (WorkEdition, "work_id", by_work(last_work)),
        "work_genres": (work_genres, "work_id", by_work(last_work)),
        "work_themes": (work_themes, "work_id", by_work(last_work)),
        "work_movements": (work_movements, "work_id", by_work(last_work)),
        "work_sources": (work_sources, "work_id", by_work(last_work)),
        "work_periods": (work_periods, "work_id",
                         lambda item: [last_work.get(t) for t in item["works"]]),
        "author_genres": (author_genres, "author_id", by_author),
        "author_movements": (author_movements, "author_id", by_author),
        "author_themes": (author_themes, "author_id", by_author),
        "author_sources": (author_sources, "author_id", by_author),
        "author_influences": (author_influences, "author_id", by_author),
        "period_movements": (period_movements, "period_id",
                             lambda item: [periods.get(item["period"])]),
        "movement_sources": (movement_sources, "movement_id",
                             lambda item: [movements.get(item["movement"])]),
    }
    removed = 0
    for key, (target, column, owners_of) in owners.items():
        ids = sorted({
            owner_id
            for payload in payloads
            for item in payload.get(key, [])
            for owner_id in owners_of(item)
            if owner_id is not None
        })
        for start in range(0, len(ids), 500):  # stay under SQLite's variable limit
            chunk = ids[start:start + 500]
            if isinstance(target, Table):
                result = session.execute(target.delete().where(target.c[column].in_(chunk)))
                removed += result.rowcount
            else:
                removed += (
                    session.query(target)
                    .filter(getattr(target, column).in_(chunk))
                    .delete(synchronize_session="fetch")
                )
    return removed


def import_relationships(session, payload: dict) -> None:
    # work_authors: [{"work": ..., "author": ..., "contribution_type": ...}]
    for item in payload.get("work_authors", []):
        work = resolve_work(session, item["work"])
        author = resolve_author(session, item["author"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_authors")
            continue
        if author is None:
            warn(f"author '{item['author']}' not found for work_authors")
            continue
        exists = (
            session.query(WorkAuthor)
            .filter_by(
                work_id=work.work_id,
                author_id=author.author_id,
                contribution_type=item["contribution_type"],
            )
            .first()
        )
        if exists is None:
            session.add(
                WorkAuthor(
                    work_id=work.work_id,
                    author_id=author.author_id,
                    contribution_type=item["contribution_type"],
                )
            )

    def link_table(table, left_kind, left_id, right_kind, right_id):
        session.execute(
            table.insert()
            .prefix_with("OR IGNORE")
            .values(**{f"{left_kind}_id": left_id, f"{right_kind}_id": right_id})
        )

    genre_by_name = {g.name: g for g in session.query(Genre).all()}
    theme_by_name = {t.name: t for t in session.query(Theme).all()}
    movement_by_name = {m.name: m for m in session.query(Movement).all()}
    period_by_name = {p.name: p for p in session.query(Period).all()}
    source_by_name = {s.title: s for s in session.query(Source).all()}
    work_by_title = {w.title: w for w in session.query(Work).all()}
    author_by_name = {a.full_name: a for a in session.query(Author).all()}

    for item in payload.get("work_genres", []):
        work = work_by_title.get(item["work"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_genres")
            continue
        for name in item["genres"]:
            genre = genre_by_name.get(name)
            if genre is None:
                warn(f"genre '{name}' not found (work '{item['work']}')")
                continue
            link_table(work_genres, "work", work.work_id, "genre", genre.genre_id)

    for item in payload.get("work_periods", []):
        period = period_by_name.get(item["period"])
        if period is None:
            warn(f"period '{item['period']}' not found")
            continue
        for title in item["works"]:
            work = work_by_title.get(title)
            if work is None:
                warn(f"work '{title}' not found for work_periods")
                continue
            link_table(work_periods, "work", work.work_id, "period", period.period_id)

    for item in payload.get("work_themes", []):
        work = work_by_title.get(item["work"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_themes")
            continue
        for name in item["themes"]:
            theme = theme_by_name.get(name)
            if theme is None:
                warn(f"theme '{name}' not found (work '{item['work']}')")
                continue
            link_table(work_themes, "work", work.work_id, "theme", theme.theme_id)

    for item in payload.get("work_movements", []):
        work = work_by_title.get(item["work"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_movements")
            continue
        for name in item["movements"]:
            movement = movement_by_name.get(name)
            if movement is None:
                warn(f"movement '{name}' not found (work '{item['work']}')")
                continue
            link_table(work_movements, "work", work.work_id, "movement", movement.movement_id)

    for item in payload.get("author_genres", []):
        author = author_by_name.get(item["author"])
        if author is None:
            warn(f"author '{item['author']}' not found for author_genres")
            continue
        for name in item["genres"]:
            genre = genre_by_name.get(name)
            if genre is None:
                warn(f"genre '{name}' not found (author '{item['author']}')")
                continue
            link_table(author_genres, "author", author.author_id, "genre", genre.genre_id)

    for item in payload.get("author_movements", []):
        author = author_by_name.get(item["author"])
        if author is None:
            warn(f"author '{item['author']}' not found for author_movements")
            continue
        for name in item["movements"]:
            movement = movement_by_name.get(name)
            if movement is None:
                warn(f"movement '{name}' not found (author '{item['author']}')")
                continue
            link_table(author_movements, "author", author.author_id, "movement", movement.movement_id)

    for item in payload.get("author_themes", []):
        author = author_by_name.get(item["author"])
        if author is None:
            warn(f"author '{item['author']}' not found for author_themes")
            continue
        for name in item["themes"]:
            theme = theme_by_name.get(name)
            if theme is None:
                warn(f"theme '{name}' not found (author '{item['author']}')")
                continue
            link_table(author_themes, "author", author.author_id, "theme", theme.theme_id)

    for item in payload.get("period_movements", []):
        period = period_by_name.get(item["period"])
        if period is None:
            warn(f"period '{item['period']}' not found for period_movements")
            continue
        for name in item["movements"]:
            movement = movement_by_name.get(name)
            if movement is None:
                warn(f"movement '{name}' not found (period '{item['period']}')")
                continue
            link_table(period_movements, "period", period.period_id, "movement", movement.movement_id)

    for item in payload.get("author_influences", []):
        author = author_by_name.get(item["author"])
        if author is None:
            warn(f"author '{item['author']}' not found for author_influences")
            continue
        for name in item["influenced_by"]:
            influencer = author_by_name.get(name)
            if influencer is None:
                warn(f"influencer '{name}' not found (author '{item['author']}')")
                continue
            link_table(
                author_influences,
                "author",
                author.author_id,
                "influenced_by_author",
                influencer.author_id,
            )

    for item in payload.get("author_sources", []):
        author = author_by_name.get(item["author"])
        if author is None:
            warn(f"author '{item['author']}' not found for author_sources")
            continue
        for name in item["sources"]:
            source = source_by_name.get(name)
            if source is None:
                warn(f"source '{name}' not found (author '{item['author']}')")
                continue
            link_table(author_sources, "author", author.author_id, "source", source.source_id)

    for item in payload.get("work_sources", []):
        work = work_by_title.get(item["work"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_sources")
            continue
        for name in item["sources"]:
            source = source_by_name.get(name)
            if source is None:
                warn(f"source '{name}' not found (work '{item['work']}')")
                continue
            link_table(work_sources, "work", work.work_id, "source", source.source_id)

    for item in payload.get("movement_sources", []):
        movement = movement_by_name.get(item["movement"])
        if movement is None:
            warn(f"movement '{item['movement']}' not found for movement_sources")
            continue
        for name in item["sources"]:
            source = source_by_name.get(name)
            if source is None:
                warn(f"source '{name}' not found (movement '{item['movement']}')")
                continue
            link_table(movement_sources, "movement", movement.movement_id, "source", source.source_id)

    for item in payload.get("work_editions", []):
        work = work_by_title.get(item["work"])
        if work is None:
            warn(f"work '{item['work']}' not found for work_editions")
            continue
        for edition in item["editions"]:
            exists = (
                session.query(WorkEdition)
                .filter_by(
                    work_id=work.work_id,
                    edition_title=edition.get("edition_title"),
                    editor=edition.get("editor"),
                    publication_year=edition.get("publication_year"),
                )
                .first()
            )
            if exists is None:
                session.add(WorkEdition(work_id=work.work_id, **edition))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="print planned entity counts without writing")
    args = parser.parse_args()

    session = get_session()
    counts = {"authors": 0, "works": 0, "periods": 0, "movements": 0,
              "genres": 0, "themes": 0, "sources": 0, "relationships": 0}
    try:
        for record in load_json_files("periods"):
            upsert_period(session, record)
            counts["periods"] += 1
        for record in load_json_files("movements"):
            upsert_movement(session, record)
            counts["movements"] += 1
        for record in load_json_files("genres"):
            upsert_genre(session, record)
            counts["genres"] += 1
        for record in load_json_files("themes"):
            upsert_theme(session, record)
            counts["themes"] += 1
        for record in load_json_files("sources"):
            upsert_source(session, record)
            counts["sources"] += 1
        for record in load_json_files("authors"):
            upsert_author(session, record)
            counts["authors"] += 1
        for record in load_json_files("works"):
            upsert_work(session, record)
            counts["works"] += 1
        payloads = load_json_files("relationships")
        rows_before = count_link_rows(session)
        cleared = clear_owned_links(session, payloads)
        for payload in payloads:
            import_relationships(session, payload)
            counts["relationships"] += 1
        session.flush()
        rows_after = count_link_rows(session)

        if args.dry_run:
            session.rollback()
            print("DRY RUN - no changes committed.")
        else:
            session.commit()
            session.execute(text("INSERT INTO works_fts(works_fts) VALUES ('rebuild')"))
            session.execute(text("INSERT INTO authors_fts(authors_fts) VALUES ('rebuild')"))
            session.commit()

        print("Import summary:")
        for key, value in counts.items():
            print(f"  {key}: {value}")
        print(f"  link rows: {rows_before} before, {rows_after} after "
              f"({cleared} owner rows replaced from the JSON)")
    finally:
        session.close()

    if warnings:
        print(f"\n{warnings.__len__()} unresolved reference(s) - see above.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
