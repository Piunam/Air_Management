from fastapi import HTTPException


def validate_baggage_weight(weight: float):

    if weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than zero."
        )

    if weight > 32:
        raise HTTPException(
            status_code=400,
            detail="Maximum baggage weight is 32 kg."
        )