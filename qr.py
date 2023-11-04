import qrcode

qr = qrcode.make("This is an example qr code")
qr.save("qr_image.png")