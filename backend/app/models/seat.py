from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String
)

from sqlalchemy.orm import relationship

from app.database import Base


class Seat(Base):
    __tablename__ = "seats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    flight_id = Column(
        Integer,
        ForeignKey("flights.id"),
        nullable=False
    )

    seat_number = Column(
        String(10),
        nullable=False
    )

    row = Column(
        Integer,
        nullable=False
    )

    seat_letter = Column(
        String(1),
        nullable=False
    )

    seat_class = Column(
        String(30),
        nullable=False
    )

    availability = Column(
        String(30),
        default="Available",
        nullable=False
    )

    is_window = Column(
        Boolean,
        default=False
    )

    is_aisle = Column(
        Boolean,
        default=False
    )

    is_emergency_exit = Column(
        Boolean,
        default=False
    )

    flight = relationship(
        "Flight",
        back_populates="seats"
    )

    booking = relationship(
        "Booking",
        back_populates="seat",
        uselist=False
    )