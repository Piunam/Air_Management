from sqlalchemy.orm import Session

from app.models.passenger import Passenger

from app.repositories.passenger_repository import PassengerRepository

from app.schemas.passenger import (
    PassengerCreate,
    PassengerUpdate
)


class PassengerService:

    @staticmethod
    def create(db: Session, data: PassengerCreate):

        if PassengerRepository.get_by_email(
            db,
            data.email
        ):
            raise ValueError("Passenger already exists")

        passenger = Passenger(**data.model_dump())

        return PassengerRepository.create(
            db,
            passenger
        )

    @staticmethod
    def get_all(db: Session):

        return PassengerRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, passenger_id: int):

        return PassengerRepository.get_by_id(
            db,
            passenger_id
        )

    @staticmethod
    def update(
        db: Session,
        passenger_id: int,
        data: PassengerUpdate
    ):

        passenger = PassengerRepository.get_by_id(
            db,
            passenger_id
        )

        if not passenger:

            return None

        for key, value in data.model_dump(
            exclude_unset=True
        ).items():

            setattr(passenger, key, value)

        PassengerRepository.update(db)

        return passenger

    @staticmethod
    def delete(
        db: Session,
        passenger_id: int
    ):

        passenger = PassengerRepository.get_by_id(
            db,
            passenger_id
        )

        if not passenger:

            return False

        PassengerRepository.delete(
            db,
            passenger
        )

        return True