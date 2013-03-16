# STA242 - Project
# eBCS attempt - image recognition and classification
# 20130222 - HCrockford

import os
from PIL import Image
from pylab import *
import numpy as np
import cv
import itertools
from skimage import filter

def get_imlist(path,ext):
	#  Returns a list of filenames for all jpg images in a directory.
        return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]


cow = array(Image.open("./cows/elanco/200.jpg"))
cv.


## Canny edge detecting

daisy = array(Image.open("./cows/elanco/200.jpg").convert("L")) 		# must be greyscale - converts.
imshow(daisy)	# heatmap like representation.
edges = filter.canny(daisy)
edges1 = filter.canny(daisy,sigma = 2)
imshow(edges)	# v noisy, picking up background
imshow(edges1)

moo = cv.LoadImage("./cows/elanco/200.jpg")
stor = cvCreateMemStorage(0)
cv.FindContours(cv.fromarray(daisy),storself.# nothing?
cv.Dra

## should use cv2
import cv2
cvin = imread(".cows/elanco/200.jpg")
# cvin2 = cv2.cvtColor(cvin, cv2.COLOR_BGR2GRAY) 			# convert color to bgay - not working?
detector = cv2.FeatureDetector_create("SIFT")
descriptor = cv2.DescriptorExtractor_create("SIFT") 		# build feature extractor.

dt = detector.detect(cvin)
imshow(cv2.drawKeypoints(cvin,dt))  	# SIFT seems to get better kp.


## WROKING - return dt.pt, .size, .angle - all things to model on? can determine which important using PCA? need to find same features in each.

grid_d = cv2.GridAdaptedFeatureDetector(detector,100) 		# extract 100 features

imshow(cv2.drawKeypoints(cvin,grid_d.detect(cvin))  		# grid holds to 100 - getting them up in head region  - crop on way in?


cv2.DescriptorMatcher_create(

## also using SURF - 
wave = cv2.SURF(400)
y = wave.detect(cvin) 		# get keypoints

imshow(cv2.drawKeypoints(cvin,y)) 	# draw them



# contour detection

from skimage import measure
moo = cv.LoadImage("./cows/elanco/200.jpg")
cont = measure.find_contours(moo,0.8)


