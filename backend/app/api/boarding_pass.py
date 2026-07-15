from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import traceback

from app.dependencies import get_db
from app.repositories.booking_repository import BookingRepository
from app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/boarding-pass",
    tags=["Boarding Pass"]
)


@router.get("/{booking_reference}")
def generate_boarding_pass(
    booking_reference: str,
    db: Session = Depends(get_db)
):
    try:
        print("\n========== BOARDING PASS REQUEST ==========")
        print(f"Booking Reference: {booking_reference}")

        # Get booking
        booking = BookingRepository.get_by_reference(
            db,
            booking_reference
        )

        print("Booking Object:", booking)

        if booking is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        # Debug relationships
        print("\n----- RELATIONSHIPS -----")

        print("Passenger:", booking.passenger)

        print("Flight:", booking.flight)

        if booking.flight:
            print("Airline:", booking.flight.airline)

        print("-------------------------")

        # Generate PDF
        pdf_path = PDFService.generate_ticket(booking)

        print("Generated PDF:", pdf_path)
        print("==========================================\n")

        return FileResponse(
            path=pdf_path,
            media_type="application/pdf",
            filename=f"{booking_reference}.pdf",
        )

    except HTTPException:
        raise

    except Exception as e:
        print("\n========== ERROR ==========")
        traceback.print_exc()
        print("Exception:", e)
        print("===========================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )