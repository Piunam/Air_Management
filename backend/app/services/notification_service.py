from typing import Optional

from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.repositories.notification_repository import NotificationRepository


class NotificationService:

    @staticmethod
    def create(
        db: Session,
        title: str,
        message: str,
        user_id: Optional[int] = None
    ) -> Notification:
        """
        Create a new notification.
        """

        notification = Notification(
            title=title,
            message=message,
            user_id=user_id
        )

        return NotificationRepository.create(
            db,
            notification
        )

    @staticmethod
    def get_all(
        db: Session
    ):
        """
        Return all notifications ordered by newest first.
        """

        return NotificationRepository.get_all(db)

    @staticmethod
    def get_unread(
        db: Session
    ):
        """
        Return only unread notifications.
        """

        return NotificationRepository.unread(db)

    @staticmethod
    def get_by_id(
        db: Session,
        notification_id: int
    ):

        return NotificationRepository.get(
            db,
            notification_id
        )

    @staticmethod
    def mark_as_read(
        db: Session,
        notification_id: int
    ):

        notification = NotificationRepository.get(
            db,
            notification_id
        )

        if notification is None:
            return None

        notification.is_read = True

        db.commit()

        db.refresh(notification)

        return notification

    @staticmethod
    def mark_all_as_read(
        db: Session
    ):

        notifications = NotificationRepository.unread(db)

        for notification in notifications:
            notification.is_read = True

        db.commit()

        return {
            "message": f"{len(notifications)} notification(s) marked as read."
        }

    @staticmethod
    def delete(
        db: Session,
        notification_id: int
    ):

        notification = NotificationRepository.get(
            db,
            notification_id
        )

        if notification is None:
            return None

        db.delete(notification)

        db.commit()

        return {
            "message": "Notification deleted successfully."
        }