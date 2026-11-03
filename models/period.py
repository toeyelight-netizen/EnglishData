"""Historical period entity."""

from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Period(Base):
    __tablename__ = "periods"

    period_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    start_year = Column(Integer)
    end_year = Column(Integer)
    description = Column(Text)
    historical_context = Column(Text)
    literary_characteristics = Column(Text)
