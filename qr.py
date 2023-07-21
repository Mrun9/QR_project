# Python | Generate QR Code using pyqrcode module
# pip install pyqrcode
# pyqrcode module is a QR code generator. 
# The module automates most of the building process for creating QR codes. 
# This module attempts to follow the QR code standard as closely as possible. 
# The terminology and the encodings used in pyqrcode come directly from the standard.

# pip install pypng


# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "file:///C:/Users/HP/Documents/Projects/QRCodes_Project/hi.html"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
#url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('hi.png', scale = 6)
