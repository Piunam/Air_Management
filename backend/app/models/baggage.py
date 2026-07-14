from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Baggage(Base):
    __tablename__ = "baggage"

    id = Column(Integer, primary_key=True)

    baggage_tag = Column(
        String(50),
        unique=True,
        nullable=False
    )

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id")
    )

    weight = Column(Integer)

    status = Column(
        String(30),
        default="Checked-In"
    )

    booking = relationship("Booking")