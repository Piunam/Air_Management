from sqlalchemy import Column, Integer, ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class CrewAssignment(Base):
    __tablename__ = "crew_assignments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    crew_id = Column(
        Integer,
        ForeignKey("crew.id")
    )

    flight_id = Column(
        Integer,
        ForeignKey("flights.id")
    )

    crew = relationship("Crew")

    flight = relationship("Flight")