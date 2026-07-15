from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.checkin import CheckIn


class CheckInRepository:

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
    def get_checkin(
        db: Session,
        booking_id: int
    ):
        return (
            db.query(CheckIn)
            .filter(
                CheckIn.booking_id == booking_id
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        checkin: CheckIn
    ):
        db.add(checkin)
        db.commit()
        db.refresh(checkin)
        return checkin

    @staticmethod
    def update(
        db: Session,
        checkin: CheckIn
    ):
        db.commit()
        db.refresh(checkin)
        return checkin

    @staticmethod
    def delete(
        db: Session,
        checkin: CheckIn
    ):
        db.delete(checkin)
        db.commit()