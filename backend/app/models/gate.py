from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Gate(Base):
    __tablename__ = "gates"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    gate_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    terminal_id = Column(
        Integer,
        ForeignKey("terminals.id")
    )

    status = Column(
        String(30),
        default="Available"
    )

    terminal = relationship(
        "Terminal",
        back_populates="gates"
    )

    flights = relationship(
        "Flight",
        back_populates="gate"
    )