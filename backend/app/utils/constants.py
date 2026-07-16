"""
Application-wide constants.
"""

# ==========================================
# BAGGAGE
# ==========================================

MAX_BAGGAGE_WEIGHT = 32.0  # kg

ECONOMY_BAG_LIMIT = 1
PREMIUM_ECONOMY_BAG_LIMIT = 2
BUSINESS_BAG_LIMIT = 2
FIRST_CLASS_BAG_LIMIT = 3


# ==========================================
# FLIGHT STATUS
# ==========================================

FLIGHT_STATUS = [
    "Scheduled",
    "Boarding",
    "Taxiing",
    "Departed",
    "In Air",
    "Landing",
    "Arrived",
    "Delayed",
    "Cancelled",
]


# ==========================================
# BOOKING STATUS
# ==========================================

BOOKING_STATUS = [
    "Pending",
    "Confirmed",
    "Cancelled",
    "Completed",
]


# ==========================================
# PAYMENT STATUS
# ==========================================

PAYMENT_STATUS = [
    "Pending",
    "Paid",
    "Failed",
    "Refunded",
]


# ==========================================
# CHECK-IN STATUS
# ==========================================

CHECKIN_STATUS = [
    "Not Checked In",
    "Checked In",
]


# ==========================================
# BOARDING STATUS
# ==========================================

BOARDING_STATUS = [
    "Waiting",
    "Boarding",
    "Completed",
]


# ==========================================
# BAGGAGE STATUS
# ==========================================

BAGGAGE_STATUS = [
    "Checked In",
    "Security",
    "Sorting",
    "Loaded",
    "In Transit",
    "Arrived",
    "Carousel",
    "Collected",
]


# ==========================================
# GATE STATUS
# ==========================================

GATE_STATUS = [
    "Available",
    "Occupied",
    "Maintenance",
]


# ==========================================
# RUNWAY STATUS
# ==========================================

RUNWAY_STATUS = [
    "Available",
    "Occupied",
    "Maintenance",
]


# ==========================================
# SEAT CLASSES
# ==========================================

SEAT_CLASSES = [
    "Economy",
    "Premium Economy",
    "Business",
    "First",
]


# ==========================================
# AIRCRAFT STATUS
# ==========================================

AIRCRAFT_STATUS = [
    "Available",
    "Maintenance",
    "Grounded",
]


# ==========================================
# WEATHER CONDITIONS
# ==========================================

WEATHER_CONDITIONS = [
    "Clear",
    "Cloudy",
    "Rain",
    "Storm",
    "Fog",
    "Snow",
]


# ==========================================
# USER ROLES
# ==========================================

USER_ROLES = [
    "Admin",
    "Manager",
    "Staff",
    "Passenger",
]