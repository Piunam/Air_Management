from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.dependencies import get_db

from app.services.seat_service import SeatService


router = APIRouter(
    prefix="/seats",
    tags=["Seats"]
)


class GenerateSeats(BaseModel):

    flight_id: int

    rows: int


@router.post("/generate")
def generate(
    request: GenerateSeats,
    db: Session = Depends(get_db)
):

    return SeatService.generate_seats(
        db,
        request.flight_id,
        request.rows
    )


@router.get("/{flight_id}")
def seat_map(
    flight_id: int,
    db: Session = Depends(get_db)
):

    return SeatService.seat_map(
        db,
        flight_id
    )


@router.post("/allocate/{booking_reference}")
def allocate(
    booking_reference: str,
    db: Session = Depends(get_db)
):

    return SeatService.allocate(
        db,
        booking_reference
    )


@router.post("/upgrade/{booking_reference}")
def upgrade(
    booking_reference: str,
    db: Session = Depends(get_db)
):

    return SeatService.upgrade(
        db,
        booking_reference
    )