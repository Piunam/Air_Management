from pydantic import BaseModel


class FlightStatusUpdate(BaseModel):
    status: str


class FlightGateUpdate(BaseModel):
    gate_id: int


class FlightDelayUpdate(BaseModel):
    departure_time: str
    arrival_time: str