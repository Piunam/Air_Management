from fastapi import FastAPI
from app.api.flights import router as flight_router
from app.api.auth import router as auth_router
from app.api.passengers import router as passenger_router
from app.api.bookings import router as booking_router
from app.api.dashboard import router as dashboard_router
from app.api.boarding_pass import router as boarding_pass_router
from app.api.checkin import router as checkin_router
from app.api.boarding import router as boarding_router
from app.api.baggage import router as baggage_router
from app.api.seats import router as seat_router
from app.api.flight_operations import router as flight_operations_router
from app.api.dashboard import router as dashboard_router
from app.api.analytics import router as analytics_router
from app.api.notifications import router as notification_router


app = FastAPI(
    title="Airport Management System",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Airport Management System Running"
    }

app.include_router(passenger_router)
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(flight_router)
app.include_router(booking_router)
app.include_router(dashboard_router)
app.include_router(boarding_pass_router)
app.include_router(checkin_router)
app.include_router(boarding_router)
app.include_router(baggage_router)
app.include_router(seat_router)
app.include_router(flight_operations_router)
app.include_router(
    dashboard_router
)
app.include_router(analytics_router)
app.include_router(
    notification_router
)
