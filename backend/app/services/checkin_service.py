from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.checkin import CheckIn
from app.repositories.checkin_repository import CheckInRepository


class CheckInService:

    @staticmethod
    def create(
        db: Session,
        booking_reference: str,
        boarding_time,
        gate: str
    ):

        booking = CheckInRepository.get_booking(
            db,
            booking_reference
        )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        existing = CheckInRepository.get_checkin(
            db,
            booking.id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Passenger already checked in"
            )

        checkin = CheckIn(
            booking_id=booking.id,
            boarding_time=boarding_time,
            gate=gate,
            status="Checked In"
        )

        return CheckInRepository.create(
            db,
            checkin
        )

    @staticmethod
    def get(
        db: Session,
        booking_reference: str
    ):

        booking = CheckInRepository.get_booking(
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
                status_code=404,
                detail="Check-in not found"
            )

        return checkin

    @staticmethod
    def update(
        db: Session,
        booking_reference: str,
        boarding_time,
        gate,
        status
    ):

        checkin = CheckInService.get(
            db,
            booking_reference
        )

        if boarding_time is not None:
            checkin.boarding_time = boarding_time

        if gate is not None:
            checkin.gate = gate

        if status is not None:
            checkin.status = status

        return CheckInRepository.update(
            db,
            checkin
        )

    @staticmethod
    def delete(
        db: Session,
        booking_reference: str
    ):

        checkin = CheckInService.get(
            db,
            booking_reference
        )

        CheckInRepository.delete(
            db,
            checkin
        )

        return {
            "message": "Check-in deleted successfully"
        }