from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    flight_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    airline_id = Column(
        Integer,
        ForeignKey("airlines.id"),
        nullable=False
    )

    source = Column(
        String(100),
        nullable=False
    )

    destination = Column(
        String(100),
        nullable=False
    )

    departure_time = Column(
        DateTime,
        nullable=False
    )

    arrival_time = Column(
        DateTime,
        nullable=False
    )

    terminal = Column(
        String(20),
        nullable=False
    )

    gate_id = Column(
        Integer,
        ForeignKey("gates.id")
    )

    aircraft_id = Column(
        Integer,
        ForeignKey("aircraft.id")
    )

    status = Column(
        String(30),
        default="Scheduled"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    airline = relationship(
        "Airline",
        back_populates="flights"
    )

    aircraft = relationship(
    "Aircraft",
    back_populates="flights"
    )

    gate = relationship(
    "Gate",
    back_populates="flights"
    )

    bookings = relationship(
        "Booking",
        back_populates="flight"
    )

    