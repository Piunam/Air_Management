import os
from reportlab.pdfgen import canvas

from app.services.qr_service import QRService


class PDFService:

    OUTPUT_DIR = "generated_tickets"

    @staticmethod
    def generate_ticket(booking):

        os.makedirs(PDFService.OUTPUT_DIR, exist_ok=True)

        passenger = booking.passenger
        flight = booking.flight
        airline = flight.airline

        # Generate QR Code
        qr_path = QRService.generate_qr(
            booking.booking_reference
        )

        pdf_path = os.path.join(
            PDFService.OUTPUT_DIR,
            f"{booking.booking_reference}.pdf"
        )

        pdf = canvas.Canvas(pdf_path)

        pdf.setTitle("Boarding Pass")

        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(70, 790, "AIRPORT BOARDING PASS")

        pdf.setFont("Helvetica", 12)

        pdf.drawString(
            70,
            750,
            f"Passenger : {passenger.first_name} {passenger.last_name}"
        )

        pdf.drawString(
            70,
            725,
            f"Flight : {flight.flight_number}"
        )

        pdf.drawString(
            70,
            700,
            f"Airline : {airline.name}"
        )

        pdf.drawString(
            70,
            675,
            f"From : {flight.source}"
        )

        pdf.drawString(
            70,
            650,
            f"To : {flight.destination}"
        )

        pdf.drawString(
            70,
            625,
            f"Departure : {flight.departure_time}"
        )

        pdf.drawString(
            70,
            600,
            f"Seat : {booking.seat_number}"
        )

        pdf.drawString(
            70,
            575,
            f"Class : {booking.travel_class}"
        )

        pdf.drawString(
            70,
            550,
            f"Booking Ref : {booking.booking_reference}"
        )

        # Insert QR Code
        if os.path.exists(qr_path):
            pdf.drawImage(
                qr_path,
                380,
                520,
                width=140,
                height=140
            )

        pdf.save()

        return pdf_path