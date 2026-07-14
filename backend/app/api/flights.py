from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.flight import (
    FlightCreate,
    FlightUpdate,
    FlightResponse
)

from app.services.flight_service import FlightService

router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


@router.post(
    "/",
    response_model=FlightResponse
)
def create_flight(
    flight: FlightCreate,
    db: Session = Depends(get_db)
):

    try:

        return FlightService.create_flight(db, flight)

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[FlightResponse]
)
def get_all_flights(
    db: Session = Depends(get_db)
):

    return FlightService.get_all(db)


@router.get(
    "/{flight_id}",
    response_model=FlightResponse
)
def get_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    flight = FlightService.get_by_id(
        db,
        flight_id
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    return flight


@router.put(
    "/{flight_id}",
    response_model=FlightResponse
)
def update_flight(
    flight_id: int,
    data: FlightUpdate,
    db: Session = Depends(get_db)
):

    flight = FlightService.update(
        db,
        flight_id,
        data
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    return flight


@router.delete(
    "/{flight_id}"
)
def delete_flight(
    flight_id: int,
    db: Session = Depends(get_db)
):

    deleted = FlightService.delete(
        db,
        flight_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    return {
        "message": "Flight deleted successfully"
    }