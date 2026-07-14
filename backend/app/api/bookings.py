from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.booking import (
    BookingCreate,
    BookingUpdate,
    BookingResponse
)

from app.services.booking_service import BookingService

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/", response_model=BookingResponse)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    try:

        return BookingService.create(
            db,
            booking
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/", response_model=list[BookingResponse])
def get_all_bookings(
    db: Session = Depends(get_db)
):

    return BookingService.get_all(db)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = BookingService.get_by_id(
        db,
        booking_id
    )

    if not booking:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.put("/{booking_id}", response_model=BookingResponse)
def update_booking(
    booking_id: int,
    data: BookingUpdate,
    db: Session = Depends(get_db)
):

    booking = BookingService.update(
        db,
        booking_id,
        data
    )

    if not booking:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    deleted = BookingService.delete(
        db,
        booking_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "message": "Booking deleted successfully"
    }