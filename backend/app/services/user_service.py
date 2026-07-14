from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.password import hash_password


class UserService:

    @staticmethod
    def register_user(db: Session, user: UserCreate):

        existing_email = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_email:
            raise ValueError("Email already exists")

        existing_username = UserRepository.get_by_username(
            db,
            user.username
        )

        if existing_username:
            raise ValueError("Username already exists")

        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password),
            full_name=user.full_name,
            phone=user.phone,
            role_id=1
        )

        return UserRepository.create(
            db,
            new_user
        )

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return UserRepository.get_by_email(
            db,
            email
        )

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return UserRepository.get_by_id(
            db,
            user_id
        )

    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all(
            db
        )