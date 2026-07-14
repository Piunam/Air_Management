from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    code = Column(
        String(10),
        unique=True,
        nullable=False
    )

    country = Column(
        String(100),
        nullable=False
    )

    flights = relationship(
        "Flight",
        back_populates="airline"
    )