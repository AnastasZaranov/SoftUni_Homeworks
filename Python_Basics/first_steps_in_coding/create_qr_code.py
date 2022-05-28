import pyqrcode
from pyqrcode import QRCode


address = "post URL here"
url = pyqrcode.create(address)
url.png("name.png", scale = 8)
