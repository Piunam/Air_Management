from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.seat import Seat
from app.models.booking import Booking

from app.repositories.seat_repository import SeatRepository
from app.utils.seat_generator import SeatGenerator
from app.services.notification_service import NotificationService


class SeatService:

    @staticmethod
    def generate_seats(
        db: Session,
        flight_id: int,
        rows: int
    ):

        existing = SeatRepository.get_all(
            db,
            flight_id
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Seats already exist for this flight."
            )

        seats = SeatGenerator.generate(
            flight_id,
            rows
        )

        SeatRepository.create_many(
            db,
            seats
        )

        return {
            "message": f"{len(seats)} seats generated successfully."
        }

    @staticmethod
    def seat_map(
        db: Session,
        flight_id: int
    ):

        seats = SeatRepository.get_all(
            db,
            flight_id
        )

        if not seats:
            raise HTTPException(
                status_code=404,
                detail="No seats found."
            )

        return seats

    @staticmethod
    def allocate(
        db: Session,
        booking_reference: str
    ):

        booking = (
            db.query(Booking)
            .filter(
                Booking.booking_reference == booking_reference
            )
            .first()
        )
        flight = booking.flight

        if flight.status == "Cancelled":
            raise HTTPException(
                status_code=400,
                detail="Flight cancelled."
            )

        if flight.status == "Departed":
            raise HTTPException(
                status_code=400,
                detail="Flight already departed."
            )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found."
            )

        if booking.seat_id:
            raise HTTPException(
                status_code=400,
                detail="Seat already allocated."
            )

        seat = (
            SeatRepository
            .get_available(
                db,
                booking.flight_id
            )
        )

        if len(seat) == 0:
            raise HTTPException(
                status_code=400,
                detail="No seats available."
            )

        seat = seat[0]

        seat.availability = "Occupied"

        booking.seat_id = seat.id

        NotificationService.create(
            db=db,
            title="Seat Allocated",
            message=f"Seat {seat.seat_number} allocated for booking {booking.booking_reference}."
        )

        db.commit()

        db.refresh(booking)

        db.refresh(seat)

        return {
            "booking_reference": booking.booking_reference,
            "seat": seat.seat_number,
            "class": seat.seat_class
        }

    @staticmethod
    def upgrade(
        db: Session,
        booking_reference: str
    ):

        booking = (
            db.query(Booking)
            .filter(
                Booking.booking_reference == booking_reference
            )
            .first()
        )

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found."
            )

        business = (
            db.query(Seat)
            .filter(
                Seat.flight_id == booking.flight_id,
                Seat.seat_class == "Business",
                Seat.availability == "Available"
            )
            .first()
        )

        if business is None:
            raise HTTPException(
                status_code=400,
                detail="Business class full."
            )

        if booking.seat:

            booking.seat.availability = "Available"

        business.availability = "Occupied"

        booking.seat_id = business.id

        booking.travel_class = "Business"

        db.commit()

        db.refresh(booking)

        return {
            "message": "Seat upgraded.",
            "seat": business.seat_number
        }