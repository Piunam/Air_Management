from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from app.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    action = Column(String(200))

    performed_by = Column(String(100))

    module = Column(String(100))

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    ip_address = Column(String(100))