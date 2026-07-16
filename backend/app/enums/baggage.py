from enum import Enum


class BaggageStatus(str, Enum):
    CHECKED_IN = "Checked In"
    SECURITY = "Security"
    SORTING = "Sorting"
    LOADED = "Loaded"
    IN_TRANSIT = "In Transit"
    ARRIVED = "Arrived"
    CAROUSEL = "Carousel"
    COLLECTED = "Collected"