from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Terminal(Base):
    __tablename__ = "terminals"

    id = Column(Integer, primary_key=True, index=True)

    terminal_name = Column(
        String(50),
        unique=True,
        nullable=False
    )

    location = Column(
        String(100)
    )

    gates = relationship(
        "Gate",
        back_populates="terminal"
    )