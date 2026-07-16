from sqlalchemy.orm import Session


class BaseRepository:

    @staticmethod
    def commit(db: Session):

        db.commit()

    @staticmethod
    def refresh(db: Session, obj):

        db.refresh(obj)

    @staticmethod
    def save(db: Session, obj):

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj