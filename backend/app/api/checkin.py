from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.checkin import (
    CheckInCreate,
    CheckInUpdate,
    CheckInResponse
)
from app.services.checkin_service import CheckInService

router = APIRouter(
    prefix="/checkin",
    tags=["Check In"]
)


@router.post(
    "/",
    response_model=CheckInResponse
)
def create_checkin(
    request: CheckInCreate,
    db: Session = Depends(get_db)
):
    return CheckInService.create(
        db,
        request.booking_reference,
        request.boarding_time,
        request.gate
    )


@router.get(
    "/{booking_reference}",
    response_model=CheckInResponse
)
def get_checkin(
    booking_reference: str,
    db: Session = Depends(get_db)
):
    return CheckInService.get(
        db,
        booking_reference
    )


@router.put(
    "/{booking_reference}",
    response_model=CheckInResponse
)
def update_checkin(
    booking_reference: str,
    request: CheckInUpdate,
    db: Session = Depends(get_db)
):
    return CheckInService.update(
        db,
        booking_reference,
        request.boarding_time,
        request.gate,
        request.status
    )


@router.delete(
    "/{booking_reference}"
)
def delete_checkin(
    booking_reference: str,
    db: Session = Depends(get_db)
):
    return CheckInService.delete(
        db,
        booking_reference
    )