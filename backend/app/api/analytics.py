from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/flights")
def flights(
    db: Session = Depends(get_db)
):
    return AnalyticsService.flights(db)


@router.get("/revenue")
def revenue(
    db: Session = Depends(get_db)
):
    return AnalyticsService.revenue(db)


@router.get("/passengers")
def passengers(
    db: Session = Depends(get_db)
):
    return AnalyticsService.passengers(db)