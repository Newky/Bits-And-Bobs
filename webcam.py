
import pygame
import Image
from pygame.locals import *
import sys
import ImageChops
import math, operator

import opencv
#this is important for capturing/displaying images
from opencv import highgui 

camera = highgui.cvCreateCameraCapture(0)

def get_image():
    im = highgui.cvQueryFrame(camera)
    # Add the line below if you need it (Ubuntu 8.04+)
    #im = opencv.cvGetMat(im)
    #convert Ipl image to PIL image
    return opencv.adaptors.Ipl2PIL(im) 

def equal(im1, im2):
    if(im1 == None or im2 == None):
	return 1;
    return ImageChops.difference(im1, im2).getbbox() is None

# Example: File: imagediff.py
def rmsdiff(im1, im2):
    if(im1 == None or im2 == None):
	return 0.0
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms

fps = 1.0
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Simple Webcam Display Program")
screen = pygame.display.get_surface()
saved_im = None
i = 0
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN:
            sys.exit(0)
    im = get_image()
    print "Change %f" %(rmsdiff(im, saved_im))
    i+=1
    saved_im = im;
    pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
    screen.blit(pg_img, (0,0))
    pygame.display.flip()
    pygame.time.delay(int(1000 * 1.0/fps))

