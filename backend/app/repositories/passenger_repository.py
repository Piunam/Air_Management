from sqlalchemy.orm import Session

from app.models.passenger import Passenger


class PassengerRepository:

    @staticmethod
    def create(db: Session, passenger: Passenger):

        db.add(passenger)

        db.commit()

        db.refresh(passenger)

        return passenger

    @staticmethod
    def get_all(db: Session):

        return db.query(Passenger).all()

    @staticmethod
    def get_by_id(db: Session, passenger_id: int):

        return db.query(Passenger).filter(
            Passenger.id == passenger_id
        ).first()

    @staticmethod
    def get_by_email(db: Session, email: str):

        return db.query(Passenger).filter(
            Passenger.email == email
        ).first()

    @staticmethod
    def delete(db: Session, passenger: Passenger):

        db.delete(passenger)

        db.commit()

    @staticmethod
    def update(db: Session):

        db.commit()