#      ReiNX Splash Script
#      use Python3 and Pillow module
#      Source code from somewhere on the internet
#      modfied by The Expert Noob / Flying Poo
#      Feel free to use it as you wish.

from PIL import Image
import sys

im = Image.open(sys.argv[1], 'r')
img = im.resize((1280, 720))
img = img.transpose(Image.FLIP_LEFT_RIGHT)
pixelMap = img.load()
pixels = []
for y in range(img.size[0]):
  for x in range(img.size[1]):
    pixels.append(pixelMap[y,x][0])
    pixels.append(pixelMap[y,x][1])
    pixels.append(pixelMap[y,x][2])
    pixels.append(0)
  for x in range(0, 48 * 4):
    pixels.append(0)
with open('splash.bin','wb') as f:
  fileSize = 720 * 1280
  f.write(bytes(x for x in pixels))
