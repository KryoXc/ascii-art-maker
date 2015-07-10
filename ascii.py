# Python script to read in an image and convert it to ascii art

import Image
import numpy as np
import sys

### TODO: add in command line arguments for script


### TODO: declare list of character lumosities in ascending order
# alpha   0   10   20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250
#chars = [' ','.','\'','`','^','"',',',':',';','I','l','!','i','>','<','~','+','_','-','?',']','[','{','}','1',')','(','|','\\','/','t','f','j','r','x','n','u','v','c','z','X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h','a','o','*','#','M','W','&','8','%','B','@','$']

# alpha
chars = [' ','.',':','-','=','+','*','#','%','@']

# open image

img = Image.open(sys.argv[1])

# convert image data to a useable form, repeat convert. redundant code
pic = np.array(img.convert('L'))

### TODO: find the dimensions of a cell. Find call to return current settings
###       from the terminal. 1080p screen is 816 pix

# note: in case of cell size not lining up, truncate
hoffset = 0
woffset = 0
w = 8
h = 16
rsum = 0
width = pic.shape[1] - (pic.shape[1] % 8)
height = pic.shape[0] - (pic.shape[0] % 16)
line = ""

## testing data for new array


print("adjusted width: " + str(width))
print("adjusted height: " + str(height))
### TODO: loop through cells, average lumosity, find corresponding character
print(pic)
while h*hoffset + 15 < height:
	while w * woffset + 7 < width: 
		for y in range(h * hoffset,( h *  hoffset) + 15):
			for x in range(w * woffset,( w * woffset) + 7):
				rsum += pic[y, x] # + 20 uncomment for brightnesss control
		rsum = rsum / (8 * 16)
		line = line + str(chars[rsum / 25])
		woffset = woffset + 1
	print(line)
	hoffset = hoffset + 1
	line = ""
	rsum = 0
	woffset = 0

	
 
### test to check greyscale conversion
#img.save('greytest.png')

### TODO(optional) write algorithm for compression for ascii video streams
