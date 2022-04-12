import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from sklearn.preprocessing import scale

qr = pyqrcode.create("QR Code")
qr.png("qr.png", scale=8)

d = decode(Image.open("qr.png"))
print(d[0].data.decode("ascii"))