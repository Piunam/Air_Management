from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    passport_number = Column(
        String(50),
        unique=True
    )

    nationality = Column(
        String(100)
    )

    phone = Column(
        String(20)
    )