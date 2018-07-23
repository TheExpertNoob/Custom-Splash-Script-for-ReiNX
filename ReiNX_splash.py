'''
Copyright (c) 2018 letsplentendo

This program is free software; you can redistribute it and/or modify it
under the terms and conditions of the GNU General Public License,
version 2, as published by the Free Software Foundation.

This program is distributed in the hope it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#TODO: make size arguments
#      fix size calculation
#      make stride fix dependent on size

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
  f.write(bytes(str(fileSize).rjust(8, "0"), 'utf-8'))
  f.write(bytes(x for x in pixels))
