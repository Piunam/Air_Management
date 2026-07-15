from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class CheckIn(Base):
    __tablename__ = "checkins"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False,
        unique=True
    )

    checked_in_at = Column(
        DateTime,
        server_default=func.now()
    )

    boarding_time = Column(
        DateTime,
        nullable=False
    )

    gate = Column(
        String(20),
        nullable=False
    )

    status = Column(
        String(30),
        default="Checked In"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    booking = relationship(
        "Booking",
        back_populates="checkin"
    )