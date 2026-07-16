from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.boarding import Boarding


class BoardingRepository:

    @staticmethod
    def get_booking(
        db: Session,
        booking_reference: str
    ):
        return (
            db.query(Booking)
            .filter(
                Booking.booking_reference == booking_reference
            )
            .first()
        )

    @staticmethod
    def get_boarding(
        db: Session,
        booking_id: int
    ):
        return (
            db.query(Boarding)
            .filter(
                Boarding.booking_id == booking_id
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        boarding: Boarding
    ):
        db.add(boarding)
        db.commit()
        db.refresh(boarding)
        return boarding

    @staticmethod
    def update(
        db: Session,
        boarding: Boarding
    ):
        db.commit()
        db.refresh(boarding)
        return boarding

    @staticmethod
    def delete(
        db: Session,
        boarding: Boarding
    ):
        db.delete(boarding)
        db.commit()