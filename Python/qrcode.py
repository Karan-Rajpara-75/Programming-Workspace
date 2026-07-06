# craft a qr code

import qrcode
qr =qrcode.make("https://www.instagram.com/")
qr.save("MyQRcode.png")
print("QR code created successfully!")  