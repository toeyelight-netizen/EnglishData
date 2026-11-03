"""Bibliographical source entity."""

from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Source(Base):
    __tablename__ = "sources"

    source_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False, unique=True)
    author_or_editor = Column(String(500))
    publisher = Column(String(255))
    publication_year = Column(Integer)
    source_type = Column(String(64))  # anthology | edition | encyclopedia | reference | archive
    url = Column(Text)
    doi_or_identifier = Column(String(255))
    accessed_date = Column(String(32))
    reliability_notes = Column(Text)
