from sqlalchemy import Column, Integer, String

from app.database import Base


class Runway(Base):
    __tablename__ = "runways"

    id = Column(Integer, primary_key=True)

    runway_number = Column(
        String(20),
        unique=True
    )

    length = Column(Integer)

    status = Column(
        String(30),
        default="Available"
    )