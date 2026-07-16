from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.models.passenger import Passenger
from app.models.booking import Booking
from app.models.payment import Payment
from app.models.baggage import Baggage


class DashboardRepository:

    @staticmethod
    def total_flights(db: Session):

        return db.query(Flight).count()

    @staticmethod
    def delayed_flights(db: Session):

        return (
            db.query(Flight)
            .filter(
                Flight.status == "Delayed"
            )
            .count()
        )

    @staticmethod
    def cancelled_flights(db: Session):

        return (
            db.query(Flight)
            .filter(
                Flight.status == "Cancelled"
            )
            .count()
        )

    @staticmethod
    def active_flights(db: Session):

        return (
            db.query(Flight)
            .filter(
                Flight.status.in_(
                    [
                        "Scheduled",
                        "Boarding",
                        "Taxiing",
                        "Departed",
                        "In Air",
                        "Landing"
                    ]
                )
            )
            .count()
        )

    @staticmethod
    def passengers(db: Session):

        return db.query(Passenger).count()
    @staticmethod
    def checked_in(db: Session):

        from app.models.checkin import CheckIn

        return db.query(CheckIn).count()


    @staticmethod
    def boarded(db: Session):

        from app.models.boarding import Boarding

        return db.query(Boarding).count()
    @staticmethod
    def bookings(db: Session):

        return db.query(Booking).count()

    @staticmethod
    def baggage(db: Session):

        return db.query(Baggage).count()

    @staticmethod
    def revenue(db: Session):

        total = (
            db.query(
                func.sum(
                    Payment.amount
                )
            )
            .scalar()
        )

        return total or 0