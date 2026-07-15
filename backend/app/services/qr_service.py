import os
import qrcode


class QRService:

    OUTPUT_FOLDER = "generated_qr"

    @classmethod
    def generate_qr(cls, booking_reference: str):

        os.makedirs(cls.OUTPUT_FOLDER, exist_ok=True)

        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

        qr.add_data(
            {
                "booking_reference": booking_reference
            }
        )

        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        filename = f"{booking_reference}.png"

        filepath = os.path.join(
            cls.OUTPUT_FOLDER,
            filename
        )

        image.save(filepath)

        return filepath