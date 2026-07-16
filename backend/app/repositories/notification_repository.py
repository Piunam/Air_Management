from sqlalchemy.orm import Session

from app.models.notification import Notification


class NotificationRepository:

    @staticmethod
    def create(
        db: Session,
        notification: Notification
    ):
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification

    @staticmethod
    def get_all(
        db: Session
    ):
        return (
            db.query(Notification)
            .order_by(Notification.created_at.desc())
            .all()
        )

    @staticmethod
    def get(
        db: Session,
        notification_id: int
    ):
        return (
            db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

    @staticmethod
    def unread(
        db: Session
    ):
        return (
            db.query(Notification)
            .filter(Notification.is_read == False)
            .order_by(Notification.created_at.desc())
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        notification: Notification
    ):
        db.commit()
        db.refresh(notification)
        return notification

    @staticmethod
    def delete(
        db: Session,
        notification: Notification
    ):
        db.delete(notification)
        db.commit()