from sqlalchemy.orm import Session

from app.models.flight import Flight


class FlightRepository:

    @staticmethod
    def create(db: Session, flight: Flight):

        db.add(flight)

        db.commit()

        db.refresh(flight)

        return flight

    @staticmethod
    def get_all(db: Session):

        return db.query(Flight).all()

    @staticmethod
    def get_by_id(db: Session, flight_id: int):

        return (
            db.query(Flight)
            .filter(Flight.id == flight_id)
            .first()
        )

    @staticmethod
    def get_by_number(db: Session, number: str):

        return (
            db.query(Flight)
            .filter(Flight.flight_number == number)
            .first()
        )

    @staticmethod
    def delete(db: Session, flight: Flight):

        db.delete(flight)

        db.commit()

    @staticmethod
    def update(db: Session):

        db.commit()