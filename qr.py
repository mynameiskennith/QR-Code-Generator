import qrcode

qr = qrcode.make("How do you do?")
qr.save("qr_image.png")