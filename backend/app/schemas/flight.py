from datetime import datetime
from pydantic import BaseModel


class FlightCreate(BaseModel):
    flight_number: str
    airline_id: int
    source: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    terminal: str
    gate_id: int
    aircraft_id: int
    status: str = "Scheduled"


class FlightUpdate(BaseModel):
    airline_id: int | None = None
    source: str | None = None
    destination: str | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    terminal: str | None = None
    gate_id: int | None = None
    aircraft_id: int | None = None
    status: str | None = None


class FlightResponse(BaseModel):
    id: int
    flight_number: str
    airline_id: int
    source: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    terminal: str
    gate_id: int | None = None
    aircraft_id: int | None = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True