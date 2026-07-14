from sqlalchemy import Column, Integer, String

from app.database import Base


class Crew(Base):
    __tablename__ = "crew"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(200),
        unique=True
    )

    phone = Column(
        String(30)
    )

    designation = Column(
        String(50)
    )

    license_number = Column(
        String(100),
        unique=True
    )

    experience_years = Column(
        Integer,
        default=0
    )

    status = Column(
        String(30),
        default="Available"
    )