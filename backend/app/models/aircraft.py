from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class Aircraft(Base):
    __tablename__ = "aircraft"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    registration_number = Column(
        String(30),
        unique=True
    )

    model = Column(
        String(100)
    )

    manufacturer = Column(
        String(100)
    )

    capacity = Column(Integer)

    airline_id = Column(
        Integer,
        ForeignKey("airlines.id")
    )

    airline = relationship("Airline")

    flights = relationship(
        "Flight",
        back_populates="aircraft"
    )