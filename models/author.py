"""Author entity."""

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, func

from .database import Base


class Author(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False, index=True)
    alternative_names = Column(Text)  # JSON list
    pseudonyms = Column(Text)  # JSON list
    birth_date = Column(String(32))
    birth_date_approximate = Column(Boolean, default=False)
    death_date = Column(String(32))
    death_date_approximate = Column(Boolean, default=False)
    birthplace = Column(Text)
    nationality_or_literary_tradition = Column(String(255))
    literary_identity = Column(String(255))
    biography = Column(Text)
    literary_profile = Column(Text)
    stylistic_characteristics = Column(Text)
    intellectual_concerns = Column(Text)
    historical_significance = Column(Text)
    major_influences = Column(Text)  # JSON list
    biographical_uncertainty = Column(Text)
    # Documented literary-historical standing. Controlled vocabulary, see
    # documentation/DATA_DICTIONARY.md: "Major / canonical", "Significant /
    # secondary", "Minor / lesser-known", "Obscure / historically neglected".
    # Nullable: installments 1-7 predate the column and keep NULL (meaning
    # "not yet graded"), so earlier work is preserved exactly as researched.
    significance_tier = Column(String(64))
    # Author-level bibliography note: documented writings that cannot honestly
    # carry a separate work record (lost texts, unverifiable fragments, works
    # whose only record is a periodical reference). Added for installment 8.
    bibliographical_notes = Column(Text)
    research_status = Column(String(32), default="complete")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
