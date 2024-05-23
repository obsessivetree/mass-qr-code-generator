import qrcode
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont
import io





# Function to generate a QR code with customized colors and rounded corners
def create_qr_code(data, fill_color, back_color, size=100):
    qr = qrcode.QRCode(
        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=14,
        border=4
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(image_factory=StyledPilImage,color_mask=SolidFillColorMask(front_color=fill_color, back_color=back_color), module_drawer=RoundedModuleDrawer() , embeded_image_path="./3.png")

    img = img.resize((size, size))

    # Create rounded corners
    rounded = Image.new('RGBA', img.size)
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + img.size, radius=15, fill=255)
    rounded.paste(img, (0, 0), mask)
    
    # Save to bytes for display
    img_bytes = io.BytesIO()
    rounded.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes

books = {
    1: 5,
    2: 6,
    3: 3
}

# Generate QR codes for the given books
# for i in books:
#     for j in range(1, books[i] + 1):
#         qr_image = create_qr_code(f'{i}-{j}', fill_color="green", back_color="white", size=100)
#         # Save the QR code image to a file
#         image_file = f'/Users/danielbeatty/Coding/python/qr_code_generator/qr_codes/qr{i}-{j}.png'
#         with open(image_file, "wb") as f:
#             f.write(qr_image.getbuffer())

# Example usage
size = 300
green = (27, 87, 43)
blue = (30, 38, 99)
red = (110, 24, 24)
fill_color = blue
back_color = (255,255,255)
qr_image = create_qr_code(f'this is a {fill_color} one with dimensions {size}x{size}', fill_color=fill_color, back_color=back_color, size=size)
# Save the QR code image to a file
image_file = f'/Users/danielbeatty/Coding/python/qr_code_generator/qr_codes/qr-{size}_color-{"blue"}.png'
with open(image_file, "wb") as f:
    f.write(qr_image.getbuffer())

Image.open(image_file).show()
