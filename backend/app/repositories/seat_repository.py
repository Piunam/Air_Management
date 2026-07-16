from sqlalchemy.orm import Session

from app.models.seat import Seat


class SeatRepository:

    @staticmethod
    def create(
        db: Session,
        seat: Seat
    ):

        db.add(seat)
        db.commit()
        db.refresh(seat)

        return seat

    @staticmethod
    def create_many(
        db: Session,
        seats: list[Seat]
    ):

        db.add_all(seats)
        db.commit()

        return seats

    @staticmethod
    def get(
        db: Session,
        seat_id: int
    ):

        return (
            db.query(Seat)
            .filter(
                Seat.id == seat_id
            )
            .first()
        )

    @staticmethod
    def get_by_number(
        db: Session,
        flight_id: int,
        seat_number: str
    ):

        return (
            db.query(Seat)
            .filter(
                Seat.flight_id == flight_id,
                Seat.seat_number == seat_number
            )
            .first()
        )

    @staticmethod
    def get_available(
        db: Session,
        flight_id: int
    ):

        return (
            db.query(Seat)
            .filter(
                Seat.flight_id == flight_id,
                Seat.availability == "Available"
            )
            .order_by(
                Seat.row,
                Seat.seat_letter
            )
            .all()
        )

    @staticmethod
    def get_all(
        db: Session,
        flight_id: int
    ):

        return (
            db.query(Seat)
            .filter(
                Seat.flight_id == flight_id
            )
            .order_by(
                Seat.row,
                Seat.seat_letter
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        seat: Seat
    ):

        db.commit()
        db.refresh(seat)

        return seat

    @staticmethod
    def delete(
        db: Session,
        seat: Seat
    ):

        db.delete(seat)
        db.commit()