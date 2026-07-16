from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    booking_reference = Column(
        String(20),
        unique=True,
        nullable=False
    )

    passenger_id = Column(
        Integer,
        ForeignKey("passengers.id"),
        nullable=False
    )

    flight_id = Column(
        Integer,
        ForeignKey("flights.id"),
        nullable=False
    )

    seat_number = Column(
        String(10)
    )

    travel_class = Column(
        String(30)
    )

    ticket_price = Column(
        Integer
    )

    payment_status = Column(
        String(30),
        default="Pending"
    )

    booking_status = Column(
        String(30),
        default="Confirmed"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    passenger = relationship(
        "Passenger",
        back_populates="bookings"
    )

    flight = relationship(
        "Flight",
        back_populates="bookings"
    )
    checkin = relationship(
    "CheckIn",
    back_populates="booking",
    uselist=False
    )
    boarding = relationship(
    "Boarding",
    back_populates="booking",
    uselist=False
    )