"""Literary movement entity."""

from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Movement(Base):
    __tablename__ = "movements"

    movement_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    start_year = Column(Integer)
    end_year = Column(Integer)
    description = Column(Text)
    historical_context = Column(Text)
    aesthetic_principles = Column(Text)
    defining_characteristics = Column(Text)
    historical_significance = Column(Text)
