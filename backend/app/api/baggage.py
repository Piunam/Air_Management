from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.baggage import (
    BaggageCreate,
    BaggageUpdate,
    BaggageResponse
)

from app.services.baggage_service import BaggageService

router = APIRouter(
    prefix="/baggage",
    tags=["Baggage"]
)


@router.post(
    "/",
    response_model=BaggageResponse
)
def create_baggage(
    request: BaggageCreate,
    db: Session = Depends(get_db)
):

    return BaggageService.create(
        db,
        request.booking_reference,
        request.baggage_tag,
        request.weight
    )


@router.get(
    "/{baggage_id}",
    response_model=BaggageResponse
)
def get_baggage(
    baggage_id: int,
    db: Session = Depends(get_db)
):

    return BaggageService.get(
        db,
        baggage_id
    )


@router.put(
    "/{baggage_id}",
    response_model=BaggageResponse
)
def update_baggage(
    baggage_id: int,
    request: BaggageUpdate,
    db: Session = Depends(get_db)
):

    return BaggageService.update(
        db,
        baggage_id,
        request.weight,
        request.status,
        request.current_location
    )


@router.delete(
    "/{baggage_id}"
)
def delete_baggage(
    baggage_id: int,
    db: Session = Depends(get_db)
):

    return BaggageService.delete(
        db,
        baggage_id
    )