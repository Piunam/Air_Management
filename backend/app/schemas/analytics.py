from pydantic import BaseModel


class FlightAnalytics(BaseModel):
    total: int
    scheduled: int
    boarding: int
    delayed: int
    departed: int
    arrived: int
    cancelled: int


class RevenueAnalytics(BaseModel):
    total_revenue: float
    total_payments: int


class PassengerAnalytics(BaseModel):
    passengers: int
    bookings: int
    checked_in: int
    boarded: int