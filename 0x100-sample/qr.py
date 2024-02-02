import os
import qrcode

img = qrcode.make("https://chat.openai.com/c/1f7f8b2f-1187-4386-9c73-f24e17e23785")
img.save("qr.png", "PNG")
os.system("open qr.png")
