# STA242 - Project
# eBCS attempt - image recognition and classification
# 20130222 - HCrockford

import os
from PIL import Image
from pylab import *
import numpy as np
import cv
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


# contour detection

from skimage import measure
moo = cv.LoadImage("./cows/elanco/200.jpg")
cont = measure.find_contours(moo,0.8)


