from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def statistics(db: Session):

        return DashboardRepository.get_statistics(db)