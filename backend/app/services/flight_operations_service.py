from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.services.notification_service import NotificationService


class FlightOperationsService:

    VALID_TRANSITIONS = {
        "Scheduled": ["Boarding", "Delayed", "Cancelled"],
        "Boarding": ["Taxiing", "Delayed", "Cancelled"],
        "Taxiing": ["Departed"],
        "Departed": ["In Air"],
        "In Air": ["Landing"],
        "Landing": ["Arrived"],
        "Arrived": [],
        "Delayed": ["Boarding", "Cancelled"],
        "Cancelled": []
    }

    @staticmethod
    def get_flight(db: Session, flight_id: int):

        flight = (
            db.query(Flight)
            .filter(Flight.id == flight_id)
            .first()
        )

        if flight is None:
            raise HTTPException(
                status_code=404,
                detail="Flight not found"
            )

        return flight

    @classmethod
    def update_status(
        cls,
        db: Session,
        flight_id: int,
        new_status: str
    ):

        flight = cls.get_flight(db, flight_id)

        allowed = cls.VALID_TRANSITIONS.get(
            flight.status,
            []
        )

        if new_status not in allowed:
            raise HTTPException(
                status_code=400,
                detail=f"Cannot change status from {flight.status} to {new_status}"
            )

        flight.status = new_status

        db.commit()
        db.refresh(flight)

        return flight

    @classmethod
    def cancel(
        cls,
        db: Session,
        flight_id: int
    ):
        NotificationService.create(
        db=db,
        title="Flight Cancelled",
        message=f"{flight.flight_number} has been cancelled."
        )

        flight = cls.get_flight(db, flight_id)

        flight.status = "Cancelled"

        db.commit()
        db.refresh(flight)

        return {
            "message": "Flight cancelled successfully."
        }

    @classmethod
    def delay(
        cls,
        db: Session,
        flight_id: int
    ):

        flight = cls.get_flight(db, flight_id)

        flight.status = "Delayed"

        db.commit()

        NotificationService.create(
            db=db,
            title="Flight Delayed",
            message=f"{flight.flight_number} has been delayed."
        )
        db.refresh(flight)

        return {
            "message": "Flight marked as delayed."
        }