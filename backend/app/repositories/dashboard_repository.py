from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.models.passenger import Passenger
from app.models.booking import Booking
from app.models.aircraft import Aircraft
from app.models.crew import Crew


class DashboardRepository:

    @staticmethod
    def get_statistics(db: Session):

        return {

            "total_flights":
                db.query(func.count(Flight.id)).scalar(),

            "total_passengers":
                db.query(func.count(Passenger.id)).scalar(),

            "total_bookings":
                db.query(func.count(Booking.id)).scalar(),

            "total_aircraft":
                db.query(func.count(Aircraft.id)).scalar(),

            "total_crew":
                db.query(func.count(Crew.id)).scalar()

        }