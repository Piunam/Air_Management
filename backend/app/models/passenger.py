from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.orm import relationship

from app.database import Base


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(String(100))

    last_name = Column(String(100))

    email = Column(
        String(200),
        unique=True
    )

    phone = Column(String(20))

    gender = Column(String(20))

    nationality = Column(String(100))

    passport_number = Column(
        String(100),
        unique=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    bookings = relationship(
        "Booking",
        back_populates="passenger"
    )