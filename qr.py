import qrcode

qr = qrcode.make("Hello World")
qr.save("qr_image.png")