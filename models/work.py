"""Work entity (literary text, including anonymous works)."""

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, func

from .database import Base


class Work(Base):
    __tablename__ = "works"

    work_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False, index=True)
    alternative_titles = Column(Text)  # JSON list
    authorship_status = Column(
        String(32), nullable=False, default="single"
    )  # single | anonymous | collaborative | attributed | disputed
    composition_date_start = Column(String(32))
    composition_date_end = Column(String(32))
    composition_date_circa = Column(Boolean)
    publication_date = Column(String(32))
    first_performance_date = Column(String(32))
    manuscript_date = Column(String(64))
    original_language = Column(String(64))
    description = Column(Text)
    summary = Column(Text)
    plot_or_argument = Column(Text)
    narrative_structure = Column(Text)
    principal_characters = Column(Text)
    literary_form = Column(String(255))
    meter_and_prosody = Column(Text)
    historical_context = Column(Text)
    literary_significance = Column(Text)
    significance = Column(Text)
    attribution_notes = Column(Text)
    bibliographical_notes = Column(Text)
    provenance_and_manuscripts = Column(Text)
    editions = Column(Text)  # JSON list
    modern_translations = Column(Text)  # JSON list
    related_works = Column(Text)  # JSON list
    manuscript_locations = Column(Text)  # JSON list
    canonical_status = Column(String(32))
    research_notes = Column(Text)
    research_status = Column(String(32), default="complete")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
