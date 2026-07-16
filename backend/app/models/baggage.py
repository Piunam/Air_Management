from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Baggage(Base):
    __tablename__ = "baggage"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False
    )

    baggage_tag = Column(
        String(50),
        unique=True,
        nullable=False
    )

    weight = Column(
        Float,
        nullable=False
    )

    status = Column(
        String(30),
        default="Checked In"
    )

    current_location = Column(
        String(100),
        default="Check-In Counter"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    booking = relationship(
        "Booking",
        back_populates="baggage"
    )