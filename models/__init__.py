"""Model package: importing this module registers all tables on Base.metadata."""

from .database import Base, DATABASE_PATH, DATABASE_URL, SessionLocal, engine, get_session
from .author import Author
from .genre import Genre
from .movement import Movement
from .period import Period
from .relationships import (
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
)
from .source import Source
from .theme import Theme
from .work import Work

__all__ = [
    "Base",
    "DATABASE_PATH",
    "DATABASE_URL",
    "SessionLocal",
    "engine",
    "get_session",
    "Author",
    "Genre",
    "Movement",
    "Period",
    "Source",
    "Theme",
    "Work",
    "WorkAuthor",
    "WorkEdition",
    "author_genres",
    "author_influences",
    "author_movements",
    "author_sources",
    "author_themes",
    "movement_sources",
    "period_movements",
    "work_genres",
    "work_movements",
    "work_periods",
    "work_sources",
    "work_themes",
]
