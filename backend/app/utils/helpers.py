import random
import string


def generate_booking_reference():

    return "".join(

        random.choices(

            string.ascii_uppercase +

            string.digits,

            k=8

        )

    )


def generate_baggage_tag():

    return "".join(

        random.choices(

            string.ascii_uppercase +

            string.digits,

            k=10

        )

    )