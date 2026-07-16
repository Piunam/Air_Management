from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.boarding import Boarding
from app.repositories.boarding_repository import BoardingRepository
from app.repositories.checkin_repository import CheckInRepository


class BoardingService:

    @staticmethod
    def create(
        db: Session,
        booking_reference: str,
        boarding_time,
        gate: str
    ):

        booking = BoardingRepository.get_booking(
            db,
            booking_reference
        )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        checkin = CheckInRepository.get_checkin(
            db,
            booking.id
        )

        if checkin is None:
            raise HTTPException(
                status_code=400,
                detail="Passenger has not checked in"
            )

        existing = BoardingRepository.get_boarding(
            db,
            booking.id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Passenger already boarded"
            )

        boarding = Boarding(
            booking_id=booking.id,
            boarding_time=boarding_time,
            gate=gate,
            boarding_status="Boarding"
        )

        return BoardingRepository.create(
            db,
            boarding
        )

    @staticmethod
    def get(
        db: Session,
        booking_reference: str
    ):

        booking = BoardingRepository.get_booking(
            db,
            booking_reference
        )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        boarding = BoardingRepository.get_boarding(
            db,
            booking.id
        )

        if boarding is None:
            raise HTTPException(
                status_code=404,
                detail="Boarding not found"
            )

        return boarding

    @staticmethod
    def update(
        db: Session,
        booking_reference: str,
        boarding_time,
        gate,
        boarding_status
    ):

        boarding = BoardingService.get(
            db,
            booking_reference
        )

        if boarding_time is not None:
            boarding.boarding_time = boarding_time

        if gate is not None:
            boarding.gate = gate

        if boarding_status is not None:
            boarding.boarding_status = boarding_status

        return BoardingRepository.update(
            db,
            boarding
        )

    @staticmethod
    def delete(
        db: Session,
        booking_reference: str
    ):

        boarding = BoardingService.get(
            db,
            booking_reference
        )

        BoardingRepository.delete(
            db,
            boarding
        )

        return {
            "message": "Boarding deleted successfully"
        }