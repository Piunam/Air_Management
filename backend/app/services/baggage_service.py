from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.baggage import Baggage
from app.repositories.baggage_repository import BaggageRepository


class BaggageService:

    @staticmethod
    def create(
        db: Session,
        booking_reference: str,
        baggage_tag: str,
        weight: float
    ):

        booking = BaggageRepository.get_booking(
            db,
            booking_reference
        )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        existing = BaggageRepository.get_by_tag(
            db,
            baggage_tag
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Baggage tag already exists"
            )

        baggage = Baggage(
            booking_id=booking.id,
            baggage_tag=baggage_tag,
            weight=weight,
            status="Checked In",
            current_location="Check-In Counter"
        )

        return BaggageRepository.create(
            db,
            baggage
        )

    @staticmethod
    def get(
        db: Session,
        baggage_id: int
    ):

        baggage = BaggageRepository.get(
            db,
            baggage_id
        )

        if baggage is None:
            raise HTTPException(
                status_code=404,
                detail="Baggage not found"
            )

        return baggage

    @staticmethod
    def update(
        db: Session,
        baggage_id: int,
        weight,
        status,
        current_location
    ):

        baggage = BaggageService.get(
            db,
            baggage_id
        )

        if weight is not None:
            baggage.weight = weight

        if status is not None:
            baggage.status = status

        if current_location is not None:
            baggage.current_location = current_location

        return BaggageRepository.update(
            db,
            baggage
        )

    @staticmethod
    def delete(
        db: Session,
        baggage_id: int
    ):

        baggage = BaggageService.get(
            db,
            baggage_id
        )

        BaggageRepository.delete(
            db,
            baggage
        )

        return {
            "message": "Baggage deleted successfully"
        }