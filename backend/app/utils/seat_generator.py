from app.models.seat import Seat


class SeatGenerator:

    LETTERS = ["A", "B", "C", "D", "E", "F"]

    @classmethod
    def generate(
        cls,
        flight_id: int,
        rows: int
    ):

        seats = []

        for row in range(1, rows + 1):

            for letter in cls.LETTERS:

                seats.append(

                    Seat(

                        flight_id=flight_id,

                        row=row,

                        seat_letter=letter,

                        seat_number=f"{row}{letter}",

                        seat_class=(
                            "Business"
                            if row <= 5
                            else "Economy"
                        ),

                        availability="Available",

                        is_window=letter in ["A", "F"],

                        is_aisle=letter in ["C", "D"],

                        is_emergency_exit=row == 12

                    )

                )

        return seats