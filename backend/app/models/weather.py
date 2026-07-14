from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from app.database import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)

    temperature = Column(Float)

    humidity = Column(Float)

    wind_speed = Column(Float)

    visibility = Column(Float)

    condition = Column(String(100))

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )