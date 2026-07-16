from pydantic import BaseModel


class DashboardOverview(BaseModel):

    total_flights: int

    active_flights: int

    delayed_flights: int

    cancelled_flights: int

    total_passengers: int

    checked_in_passengers: int

    boarded_passengers: int

    total_bookings: int

    baggage_checked_in: int

    total_revenue: float