from pydantic import BaseModel


class DashboardStatistics(BaseModel):

    total_flights: int

    total_passengers: int

    total_bookings: int

    total_aircraft: int

    total_crew: int