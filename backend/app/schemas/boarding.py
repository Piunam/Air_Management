from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BoardingCreate(BaseModel):

    booking_reference: str
    boarding_time: datetime
    gate: str


class BoardingUpdate(BaseModel):

    boarding_time: Optional[datetime] = None
    gate: Optional[str] = None
    boarding_status: Optional[str] = None


class BoardingResponse(BaseModel):

    id: int
    booking_id: int
    boarding_time: datetime
    gate: str
    boarding_status: str

    class Config:
        from_attributes = True