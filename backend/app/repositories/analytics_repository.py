from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.models.payment import Payment
from app.models.passenger import Passenger
from app.models.booking import Booking
from app.models.checkin import CheckIn
from app.models.boarding import Boarding


class AnalyticsRepository:

    @staticmethod
    def flight_stats(db: Session):

        statuses = [
            "Scheduled",
            "Boarding",
            "Delayed",
            "Departed",
            "Arrived",
            "Cancelled"
        ]

        data = {
            "total": db.query(Flight).count()
        }

        for status in statuses:
            data[status.lower().replace(" ", "_")] = (
                db.query(Flight)
                .filter(Flight.status == status)
                .count()
            )

        return data

    @staticmethod
    def revenue(db: Session):

        revenue = db.query(
            func.sum(Payment.amount)
        ).scalar()

        return {
            "total_revenue": revenue or 0,
            "total_payments": db.query(Payment).count()
        }

    @staticmethod
    def passengers(db: Session):

        return {
            "passengers": db.query(Passenger).count(),
            "bookings": db.query(Booking).count(),
            "checked_in": db.query(CheckIn).count(),
            "boarded": db.query(Boarding).count()
        }