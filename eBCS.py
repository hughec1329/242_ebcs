# STA242 - Project
# eBCS attempt - image recognition and classification
# 20130222 - HCrockford

import os
from PIL import Image
from pylab import *
import numpy as np
import cv

def get_imlist(path,ext):
	#  Returns a list of filenames for all jpg images in a directory.
        return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]


cow = array(Image.open("./cows/elanco/200.jpg"))
cv.

