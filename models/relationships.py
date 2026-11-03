"""Association (many-to-many) tables and the WorkEdition entity.

Two association tables beyond the project spec are added for normalization:
``work_genres`` and ``work_periods`` (the spec requires works to carry genre and
period data, and these are many-to-many in nature).
"""

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text

from .database import Base

author_themes = Table(
    "author_themes",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
    Column("theme_id", Integer, ForeignKey("themes.theme_id"), primary_key=True),
)

work_themes = Table(
    "work_themes",
    Base.metadata,
    Column("work_id", Integer, ForeignKey("works.work_id"), primary_key=True),
    Column("theme_id", Integer, ForeignKey("themes.theme_id"), primary_key=True),
)

author_movements = Table(
    "author_movements",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
    Column("movement_id", Integer, ForeignKey("movements.movement_id"), primary_key=True),
)

work_movements = Table(
    "work_movements",
    Base.metadata,
    Column("work_id", Integer, ForeignKey("works.work_id"), primary_key=True),
    Column("movement_id", Integer, ForeignKey("movements.movement_id"), primary_key=True),
)

author_genres = Table(
    "author_genres",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.genre_id"), primary_key=True),
)

work_genres = Table(
    "work_genres",
    Base.metadata,
    Column("work_id", Integer, ForeignKey("works.work_id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.genre_id"), primary_key=True),
)

work_periods = Table(
    "work_periods",
    Base.metadata,
    Column("work_id", Integer, ForeignKey("works.work_id"), primary_key=True),
    Column("period_id", Integer, ForeignKey("periods.period_id"), primary_key=True),
)

author_sources = Table(
    "author_sources",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
    Column("source_id", Integer, ForeignKey("sources.source_id"), primary_key=True),
)

work_sources = Table(
    "work_sources",
    Base.metadata,
    Column("work_id", Integer, ForeignKey("works.work_id"), primary_key=True),
    Column("source_id", Integer, ForeignKey("sources.source_id"), primary_key=True),
)

movement_sources = Table(
    "movement_sources",
    Base.metadata,
    Column("movement_id", Integer, ForeignKey("movements.movement_id"), primary_key=True),
    Column("source_id", Integer, ForeignKey("sources.source_id"), primary_key=True),
)

period_movements = Table(
    "period_movements",
    Base.metadata,
    Column("period_id", Integer, ForeignKey("periods.period_id"), primary_key=True),
    Column("movement_id", Integer, ForeignKey("movements.movement_id"), primary_key=True),
)

author_influences = Table(
    "author_influences",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
    Column(
        "influenced_by_author_id",
        Integer,
        ForeignKey("authors.author_id"),
        primary_key=True,
    ),
)


class WorkAuthor(Base):
    """Many-to-many author/work relationship with a contribution type.

    Supports authors, co-authors, translators, editors, adaptors and disputed
    attributions.
    """

    __tablename__ = "work_authors"

    work_id = Column(Integer, ForeignKey("works.work_id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.author_id"), primary_key=True)
    contribution_type = Column(String(64), primary_key=True)


class WorkEdition(Base):
    __tablename__ = "work_editions"

    work_edition_id = Column(Integer, primary_key=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey("works.work_id"), nullable=False, index=True)
    edition_title = Column(String(500))
    editor = Column(String(500))
    publisher = Column(String(255))
    publication_year = Column(Integer)
    edition_notes = Column(Text)
