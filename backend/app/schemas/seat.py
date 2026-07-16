from typing import Optional

from pydantic import BaseModel


class SeatCreate(BaseModel):
    flight_id: int
    row: int
    seat_letter: str
    seat_class: str
    is_window: bool = False
    is_aisle: bool = False
    is_emergency_exit: bool = False


class SeatUpdate(BaseModel):
    availability: Optional[str] = None


class SeatResponse(BaseModel):
    id: int
    flight_id: int
    seat_number: str
    row: int
    seat_letter: str
    seat_class: str
    availability: str
    is_window: bool
    is_aisle: bool
    is_emergency_exit: bool

    class Config:
        from_attributes = True