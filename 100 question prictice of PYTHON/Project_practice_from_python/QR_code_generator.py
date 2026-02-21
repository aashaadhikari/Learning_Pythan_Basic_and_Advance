# Qr code generator in python 


import qrcode as qr

image = qr.make("https://www.facebook.com/")

image.save("FaceBook.png")