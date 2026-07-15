from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/statistics")
def statistics(
    db: Session = Depends(get_db)
):

    return DashboardService.statistics(db)