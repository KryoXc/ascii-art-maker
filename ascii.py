# Python script to read in an image and convert it to ascii art

from PIL import Image
import numpy as np
import sys
#import argparse

### TODO: add in command line arguments for script
#parser = argparse.ArgumentParser(description='convert image to ascii art.')

#parser.add_argument('image', type=String, help='The file to convert.')

gran = 25

#if sys.argv[3] != None:
	#chars = arg[3]
#	if sys.argv[4] != None:
#		gran = sys,argv[4]

# large charset(70)
chars = [' ','.','\'','`','^','"',',',':',';','I','l','!','i','>','<','~','+','_','-','?',']','[','{','}','1',')','(','|','\\','/','t','f','j','r','x','n','u','v','c','z','X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h','a','o','*','#','M','W','&','8','%','B','$','@']

# medium charset(50)
#chars = [' ','.','^','"',',',':',';','l','i','>','~','+','_','-','[','}','1','(','|','/','t','f','j','r','x','n','c','z','X','U','C','L','Q','O','Z','w','q','d','k','h','a','o','*','#','W','&','8','%','$','@']

# small charset (10)
#chars = [' ','.',':','-','=','+','*','#','%','@']

# open image
img = Image.open(sys.argv[1])

# convert image data to a useable form, repeat convert. redundant code
pic = np.array(img.convert('L'))

### 1080p screen is 8 x 16 pix

w = 8
h = 16
rsum = 0

woffset = 0
hoffset = 0

# truncate dimensions to fit cells
width = pic.shape[1] - (pic.shape[1] % 8)
height = pic.shape[0] - (pic.shape[0] % 16)

line = ""



print("adjusted width: " + str(width))
print("adjusted height: " + str(height))

#debugging line
#print(pic)

while h*hoffset + 15 < height:
	while w * woffset + 7 < width: 
		for y in range(h * hoffset,( h *  hoffset) + 15):
			for x in range(w * woffset,( w * woffset) + 7):
				rsum += pic[y, x] #- 100 #uncomment for brightnesss control
		rsum = rsum / (8 * 16)
		line = line + str(chars[rsum / gran])
		woffset = woffset + 1
	print(line)
	hoffset = hoffset + 1
	line = ""
	rsum = 0
	woffset = 0

### TODO(optional) write algorithm for compression for ascii video streams
