from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.passenger import (
    PassengerCreate,
    PassengerUpdate,
    PassengerResponse
)

from app.services.passenger_service import PassengerService

router = APIRouter(
    prefix="/passengers",
    tags=["Passengers"]
)


@router.post(
    "/",
    response_model=PassengerResponse
)
def create_passenger(
    passenger: PassengerCreate,
    db: Session = Depends(get_db)
):

    try:

        return PassengerService.create(
            db,
            passenger
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[PassengerResponse]
)
def get_all_passengers(
    db: Session = Depends(get_db)
):

    return PassengerService.get_all(db)


@router.get(
    "/{passenger_id}",
    response_model=PassengerResponse
)
def get_passenger(
    passenger_id: int,
    db: Session = Depends(get_db)
):

    passenger = PassengerService.get_by_id(
        db,
        passenger_id
    )

    if not passenger:

        raise HTTPException(
            status_code=404,
            detail="Passenger not found"
        )

    return passenger


@router.put(
    "/{passenger_id}",
    response_model=PassengerResponse
)
def update_passenger(
    passenger_id: int,
    data: PassengerUpdate,
    db: Session = Depends(get_db)
):

    passenger = PassengerService.update(
        db,
        passenger_id,
        data
    )

    if not passenger:

        raise HTTPException(
            status_code=404,
            detail="Passenger not found"
        )

    return passenger


@router.delete(
    "/{passenger_id}"
)
def delete_passenger(
    passenger_id: int,
    db: Session = Depends(get_db)
):

    deleted = PassengerService.delete(
        db,
        passenger_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Passenger not found"
        )

    return {
        "message": "Passenger deleted successfully"
    }