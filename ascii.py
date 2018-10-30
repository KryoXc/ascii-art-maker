# Python script to read in an image and convert it to ascii art

from PIL import Image
import numpy as np
import sys, os, argparse

gran = 25

#chars = ' `^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
chars = " .:-=+*#%@"

def open_image(path):
    img = Image.open(sys.argv[1])
    return np.array(img.convert('L'))


def generate_ascii(image, gamma):
    w = 8
    h = 16
    rsum = 0

    woffset = 0
    hoffset = 0

    # truncate dimensions to fit cells
    width = image.shape[1] - (image.shape[1] % 8)
    height = image.shape[0] - (image.shape[0] % 16)

    line = ""

    #print("adjusted width: " + str(width))
    #print("adjusted height: " + str(height))

    while h*hoffset + 15 < height:
	    while w * woffset + 7 < width: 
		    for y in range(h * hoffset,( h *  hoffset) + 15):
			    for x in range(w * woffset,( w * woffset) + 7):
				    rsum += image[y, x] #- gamma #uncomment for brightnesss control
		    rsum = rsum / (8 * 16)
		    line = line + str(chars[int(rsum / gran)])
		    woffset = woffset + 1

	    print(line)
	    hoffset = hoffset + 1
	    line = ""
	    rsum = 0
	    woffset = 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='convert image to ascii art.')
    parser.add_argument('image', type=str, help='The file to convert.',)
    parser.add_argument('--verbose', '-v', help="Increase output verbosity", action='store_true')
    parser.add_argument('--gamma', '-g', type=int, help='gamma offset')
    args = parser.parse_args()

    if not os.path.isfile(args.image):
        parser.print_help()
        sys.exit(1)
    else:
        image = open_image(args.image)

    if args.gamma is None:
        args.gamma = 0

    generate_ascii(image, args.gamma)

