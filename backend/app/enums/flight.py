from enum import Enum


class FlightStatus(str, Enum):
    SCHEDULED = "Scheduled"
    BOARDING = "Boarding"
    TAXIING = "Taxiing"
    DEPARTED = "Departed"
    IN_AIR = "In Air"
    LANDING = "Landing"
    ARRIVED = "Arrived"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"