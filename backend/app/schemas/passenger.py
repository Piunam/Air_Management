from datetime import datetime

from pydantic import BaseModel, EmailStr


class PassengerCreate(BaseModel):

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    gender: str

    nationality: str

    passport_number: str


class PassengerUpdate(BaseModel):

    first_name: str | None = None

    last_name: str | None = None

    email: EmailStr | None = None

    phone: str | None = None

    gender: str | None = None

    nationality: str | None = None

    passport_number: str | None = None


class PassengerResponse(BaseModel):

    id: int

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    gender: str

    nationality: str

    passport_number: str

    created_at: datetime

    class Config:
        from_attributes = True