from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get("/")
def get_notifications(
    db: Session = Depends(get_db)
):
    return NotificationService.get_all(db)


@router.get("/unread")
def unread_notifications(
    db: Session = Depends(get_db)
):
    return NotificationService.get_unread(db)


@router.put("/{notification_id}/read")
def mark_read(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = NotificationService.mark_as_read(
        db,
        notification_id
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found."
        )

    return notification


@router.put("/read-all")
def mark_all_read(
    db: Session = Depends(get_db)
):
    return NotificationService.mark_all_as_read(db)


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = NotificationService.delete(
        db,
        notification_id
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found."
        )

    return notification