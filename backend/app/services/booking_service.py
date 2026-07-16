from sqlalchemy.orm import Session

from app.models.booking import Booking

from app.repositories.booking_repository import BookingRepository

from app.schemas.booking import (
    BookingCreate,
    BookingUpdate
)

from app.services.notification_service import NotificationService


class BookingService:

    @staticmethod
    def create(db: Session, data: BookingCreate):

        if BookingRepository.get_by_reference(
            db,
            data.booking_reference
        ):
            raise ValueError("Booking already exists")

        booking = Booking(**data.model_dump())

        booking = BookingRepository.create(
            db,
            booking
        )

        NotificationService.create(
            db=db,
            title="Booking Confirmed",
            message=f"Booking {booking.booking_reference} has been confirmed."
        )

        return booking

    @staticmethod
    def get_all(db: Session):

        return BookingRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, booking_id: int):

        return BookingRepository.get_by_id(
            db,
            booking_id
        )

    @staticmethod
    def update(db: Session, booking_id: int, data: BookingUpdate):

        booking = BookingRepository.get_by_id(
            db,
            booking_id
        )

        if not booking:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(booking, key, value)

        BookingRepository.update(db)

        return booking

    @staticmethod
    def delete(db: Session, booking_id: int):

        booking = BookingRepository.get_by_id(
            db,
            booking_id
        )

        if not booking:
            return False

        BookingRepository.delete(
            db,
            booking
        )

        return True