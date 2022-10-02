#install all the necessagry libraries needed
# create function that collects the text and covert it to qrcode
# save qrcode as an image
#run the function

from asyncio import constants
from turtle import fillcolor
import qrcode

def generate_code(text):
    qr=qrcode.QRCode(
        version =1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("qrimg.png")

url=input("Enter your url:")
generate_code(url)   