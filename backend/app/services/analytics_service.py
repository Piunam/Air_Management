from sqlalchemy.orm import Session

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    def flights(db: Session):
        return AnalyticsRepository.flight_stats(db)

    @staticmethod
    def revenue(db: Session):
        return AnalyticsRepository.revenue(db)

    @staticmethod
    def passengers(db: Session):
        return AnalyticsRepository.passengers(db)