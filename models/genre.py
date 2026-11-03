"""Genre entity with optional parent genre (hierarchy)."""

from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .database import Base


class Genre(Base):
    __tablename__ = "genres"

    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    parent_genre_id = Column(Integer, ForeignKey("genres.genre_id"))
    description = Column(Text)
    historical_development = Column(Text)
