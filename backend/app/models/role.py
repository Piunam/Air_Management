from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String




class Role(Base):
    __tablename__ = "roles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(50),
        unique=True,
        nullable=False
    )

    users = relationship(
        "User",
        back_populates="role"
    )