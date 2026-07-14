from sqlalchemy.orm import Session

from app.models.flight import Flight

from app.repositories.flight_repository import FlightRepository

from app.schemas.flight import FlightCreate, FlightUpdate


class FlightService:

    @staticmethod
    def create_flight(db: Session, data: FlightCreate):

        if FlightRepository.get_by_number(
            db,
            data.flight_number
        ):
            raise ValueError("Flight already exists")

        flight = Flight(

            flight_number=data.flight_number,

            airline=data.airline,

            source=data.source,

            destination=data.destination,

            departure_time=data.departure_time,

            arrival_time=data.arrival_time,

            terminal=data.terminal,

            gate=data.gate,

            aircraft=data.aircraft,

            status=data.status

        )

        return FlightRepository.create(db, flight)

    @staticmethod
    def get_all(db: Session):

        return FlightRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, flight_id: int):

        return FlightRepository.get_by_id(db, flight_id)

    @staticmethod
    def update(db: Session, flight_id: int, data: FlightUpdate):

        flight = FlightRepository.get_by_id(db, flight_id)

        if not flight:

            return None

        for key, value in data.model_dump(exclude_unset=True).items():

            setattr(flight, key, value)

        FlightRepository.update(db)

        return flight

    @staticmethod
    def delete(db: Session, flight_id: int):

        flight = FlightRepository.get_by_id(db, flight_id)

        if not flight:

            return False

        FlightRepository.delete(db, flight)

        return True