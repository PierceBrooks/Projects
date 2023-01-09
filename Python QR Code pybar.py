from pyzbar.pyzbar import decode

from PIL import Image

img = Image.open('C:/Users/mrpie/OneDrive/Pictures/PPNF/myqrcode.png')

result = decode(img)

print(result)