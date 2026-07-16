from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.baggage import Baggage


class BaggageRepository:

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
    def get_by_tag(
        db: Session,
        baggage_tag: str
    ):
        return (
            db.query(Baggage)
            .filter(
                Baggage.baggage_tag == baggage_tag
            )
            .first()
        )

    @staticmethod
    def get(
        db: Session,
        baggage_id: int
    ):
        return (
            db.query(Baggage)
            .filter(
                Baggage.id == baggage_id
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        baggage: Baggage
    ):
        db.add(baggage)
        db.commit()
        db.refresh(baggage)
        return baggage

    @staticmethod
    def update(
        db: Session,
        baggage: Baggage
    ):
        db.commit()
        db.refresh(baggage)
        return baggage

    @staticmethod
    def delete(
        db: Session,
        baggage: Baggage
    ):
        db.delete(baggage)
        db.commit()