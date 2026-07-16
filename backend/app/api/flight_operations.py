from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.dependencies import get_db
from app.services.flight_operations_service import FlightOperationsService

router = APIRouter(
    prefix="/flight-operations",
    tags=["Flight Operations"]
)


class FlightStatusUpdate(BaseModel):
    status: str


@router.put("/{flight_id}/status")
def update_status(
    flight_id: int,
    request: FlightStatusUpdate,
    db: Session = Depends(get_db)
):

    return FlightOperationsService.update_status(
        db,
        flight_id,
        request.status
    )


@router.put("/{flight_id}/delay")
def delay_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    return FlightOperationsService.delay(
        db,
        flight_id
    )


@router.put("/{flight_id}/cancel")
def cancel_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    return FlightOperationsService.cancel(
        db,
        flight_id
    )


@router.get("/{flight_id}")
def get_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    return FlightOperationsService.get_flight(
        db,
        flight_id
    )