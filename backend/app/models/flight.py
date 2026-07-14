from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

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

    departure = Column(
        String(100)
    )

    arrival = Column(
        String(100)
    )

    status = Column(
        String(30)
    )