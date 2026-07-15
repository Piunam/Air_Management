from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CheckInCreate(BaseModel):
    booking_reference: str
    boarding_time: datetime
    gate: str


class CheckInUpdate(BaseModel):
    boarding_time: Optional[datetime] = None
    gate: Optional[str] = None
    status: Optional[str] = None


class CheckInResponse(BaseModel):
    id: int
    booking_id: int
    checked_in_at: datetime
    boarding_time: datetime
    gate: str
    status: str

    class Config:
        from_attributes = True