#Time pass QRCODE generator

import qrcode
from PIL import Image

def generate_qr_code(data, file_path=None):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code object
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code object
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file if a file path is provided
    if file_path:
        img.save(file_path)
        print(f"QR code saved to {file_path}")
    else:
        # Otherwise, show the image using the default image viewer
        img.show()

# Example usage
data = "https://www.example.com"  # Replace with the data you want to encode in the QR code
file_path = "qrcode.png"  # Path to save the QR code image, or None to display it

generate_qr_code(data, file_path)
