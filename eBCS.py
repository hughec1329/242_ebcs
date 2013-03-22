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

## should use cv2 - needed to cmake - compile
import cv2
cvin = imread(".cows/elanco/200.jpg")
# cvin2 = cv2.cvtColor(cvin, cv2.COLOR_BGR2GRAY) 			# convert color to bgay - not working?
detector = cv2.FeatureDetector_create("SIFT")
descriptor = cv2.DescriptorExtractor_create("SIFT") 		# build feature extractor.

dt = detector.detect(cvin)
imshow(cv2.drawKeypoints(cvin,dt))  	# SIFT seems to get better kp.

## WORKING - return dt.pt, .size, .angle - all things to model on? can determine which important using PCA? need to find same features in each.

grid_d = cv2.GridAdaptedFeatureDetector(detector,100) 		# extract 100 features

imshow(cv2.drawKeypoints(cvin,grid_d.detect(cvin))  		# grid holds to 100 - getting them up in head region  - crop on way in?

cv2.DescriptorMatcher_create(

## also using SURF - 
wave = cv2.SURF(400)
y = wave.detect(cvin) 		# get keypoints

imshow(cv2.drawKeypoints(cvin,y)) 	# draw them

# moments
cv2.moments(daisy)

## using daisy - greyscale from above
daisy_kp = detector.detect(daisy)

# contour detection

from skimage import measure
moo = cv.LoadImage("./cows/elanco/200.jpg")
cont = measure.find_contours(moo,0.8)

daisy=imread("./cows/elanco/200.jpg")
cv.Flip(cv.fromarray(daisy))
daisygrey = cv2.cvtColor(daisy,cv2.COLOR_RGB2GRAY)

# for writeup
import matplotlib.pyplot as plt

cow = imread("./cows/real/25.png")
cv.Flip(cv.fromarray(cow))
imshow(cow)
blurcow = cv2.GaussianBlur(cow,(31,31)) 	# apply filter
blurgrey = cv2.cvtColor(blurcow,cv2.COLOR_RGB2GRAY)
imshow(blurgrey,cmap = cm.Greys_r)					# show blurchow

plt.hist(blurgrey)
bcmin = 132 - blurgrey 
blackcow = np.where(blurgrey>180,blurgrey-180,blurgrey)
plt.hist(blackcow)

imshow(blackcow,cmap = cm.Greys_r)					# show blackcow - wrong - should be blacker?- maybe how its using cmap to disp?

daisy_cont = cv2.findContours(blurgrey,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 	# need a black background w white cow - threshold?Z
cv2.drawContours(daisy,i,-1,(0,255,0),3)
