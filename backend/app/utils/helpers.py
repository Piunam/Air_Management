import random
import string
import uuid


def booking_reference():
    return str(uuid.uuid4()).split("-")[0].upper()


def baggage_tag():
    return str(uuid.uuid4()).split("-")[1].upper()


def payment_reference():
    return str(uuid.uuid4()).split("-")[2].upper()


def generate_booking_reference():
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=8
        )
    )


def generate_baggage_tag():
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=10
        )
    )


def generate_payment_reference():
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=12
        )
    )