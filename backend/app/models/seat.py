from sqlalchemy import Column, Integer, String, ForeignKey

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
        ForeignKey("flights.id")
    )

    seat_number = Column(
        String(10)
    )

    seat_class = Column(
        String(30)
    )

    availability = Column(
        String(30),
        default="Available"
    )

    flight = relationship("Flight")