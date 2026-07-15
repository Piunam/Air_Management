from fastapi import APIRouter

from app.services.qr_service import QRService

router = APIRouter(
    prefix="/boarding",
    tags=["Boarding"],
)


@router.get("/qr/{booking_reference}")
def generate_qr(
    booking_reference: str,
):

    path = QRService.generate(
        booking_reference
    )

    return {
        "message": "QR Code Generated",
        "path": path,
    }