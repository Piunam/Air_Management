from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def overview(db: Session):

        return {

            "total_flights":
                DashboardRepository.total_flights(db),

            "active_flights":
                DashboardRepository.active_flights(db),

            "delayed_flights":
                DashboardRepository.delayed_flights(db),

            "cancelled_flights":
                DashboardRepository.cancelled_flights(db),

            "total_passengers":
                DashboardRepository.passengers(db),

            "checked_in_passengers":
                DashboardRepository.checked_in(db),

            "boarded_passengers":
                DashboardRepository.boarded(db),

            "total_bookings":
                DashboardRepository.bookings(db),

            "baggage_checked_in":
                DashboardRepository.baggage(db),

            "total_revenue":
                DashboardRepository.revenue(db)

        }