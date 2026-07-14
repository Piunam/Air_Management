from datetime import datetime

from pydantic import BaseModel


class BookingCreate(BaseModel):

    booking_reference: str

    passenger_id: int

    flight_id: int

    seat_number: str

    travel_class: str

    booking_status: str = "Confirmed"


class BookingUpdate(BaseModel):

    seat_number: str | None = None

    travel_class: str | None = None

    booking_status: str | None = None


class BookingResponse(BaseModel):

    id: int

    booking_reference: str

    passenger_id: int

    flight_id: int

    seat_number: str

    travel_class: str

    booking_status: str

    created_at: datetime

    class Config:
        from_attributes = True