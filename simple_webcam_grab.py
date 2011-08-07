import opencv
import sys
#this is important for capturing/displaying images
from opencv import highgui 

import time

def get_image():
    im = highgui.cvQueryFrame(camera)
    # Add the line below if you need it (Ubuntu 8.04+)
    #im = opencv.cvGetMat(im)
    #convert Ipl image to PIL image
    return opencv.adaptors.Ipl2PIL(im) 


if __name__ == "__main__":
	if len(sys.argv) > 1:
		fname = sys.argv[1]
	else:
		fname = str(time.time()) + ".png"
	camera = highgui.cvCreateCameraCapture(0)
	im = get_image()
	im.save(fname, "JPEG")



