from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)

    aircraft_id = Column(
        Integer,
        ForeignKey("aircraft.id")
    )

    maintenance_type = Column(
        String(100)
    )

    description = Column(
        String(500)
    )

    scheduled_date = Column(
        DateTime
    )

    completed_date = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String(30),
        default="Scheduled"
    )

    aircraft = relationship("Aircraft")