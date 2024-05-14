import qrcode
from PIL import Image
import io

# Function to generate a QR code with customized colors
def create_qr_code(data, fill_color, back_color, i, j):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save to bytes for display
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes
books = {
    1:5,
    2:6,
    3:3}
for i in books:
    for j in range(1, books[i]+1):
        qr_image = create_qr_code(f'{i}-{j}', fill_color="green", back_color="white", i=i, j=j)
        # Save the QR code image to a file
        image_file = f'/Users/danielbeatty/Coding/python/qr_code_generator/qr_codes/qr{i}-{j}.png'
        with open(image_file, "wb") as f:
            f.write(qr_image.getbuffer())

        # Image.open(image_file).show()

