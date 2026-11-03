"""Theme entity with optional parent theme (hierarchy)."""

from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .database import Base


class Theme(Base):
    __tablename__ = "themes"

    theme_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    parent_theme_id = Column(Integer, ForeignKey("themes.theme_id"))
    description = Column(Text)
