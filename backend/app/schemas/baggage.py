from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaggageCreate(BaseModel):

    booking_reference: str
    baggage_tag: str
    weight: float


class BaggageUpdate(BaseModel):

    weight: Optional[float] = None
    status: Optional[str] = None
    current_location: Optional[str] = None


class BaggageResponse(BaseModel):

    id: int
    booking_id: int
    baggage_tag: str
    weight: float
    status: str
    current_location: str
    created_at: datetime

    class Config:
        from_attributes = True