from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_method = Column(
        String(50),
        nullable=False
    )

    transaction_id = Column(
        String(100),
        unique=True,
        nullable=False
    )

    payment_status = Column(
        String(30),
        default="Pending"
    )

    payment_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    booking = relationship("Booking")