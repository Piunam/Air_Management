from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.boarding import (
    BoardingCreate,
    BoardingUpdate,
    BoardingResponse
)

from app.services.boarding_service import BoardingService

router = APIRouter(
    prefix="/boarding",
    tags=["Boarding"]
)


@router.post(
    "/",
    response_model=BoardingResponse
)
def create_boarding(
    request: BoardingCreate,
    db: Session = Depends(get_db)
):

    return BoardingService.create(
        db,
        request.booking_reference,
        request.boarding_time,
        request.gate
    )


@router.get(
    "/{booking_reference}",
    response_model=BoardingResponse
)
def get_boarding(
    booking_reference: str,
    db: Session = Depends(get_db)
):

    return BoardingService.get(
        db,
        booking_reference
    )


@router.put(
    "/{booking_reference}",
    response_model=BoardingResponse
)
def update_boarding(
    booking_reference: str,
    request: BoardingUpdate,
    db: Session = Depends(get_db)
):

    return BoardingService.update(
        db,
        booking_reference,
        request.boarding_time,
        request.gate,
        request.boarding_status
    )


@router.delete(
    "/{booking_reference}"
)
def delete_boarding(
    booking_reference: str,
    db: Session = Depends(get_db)
):

    return BoardingService.delete(
        db,
        booking_reference
    )