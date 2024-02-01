#  libopencv-dev and python-opencv are installed systemwide
import cv2

print("")
print("Hi... This is Image Manipulation by Python")
print("")

import numpy as np
import matplotlib.pyplot as plt 


from skimage import img_as_uint
from skimage.io import imshow, imread
from skimage.color import rgb2hsv
from skimage.color import rgb2gray

array_1 = np.array([[255, 0], [0, 255]])

imshow(array_1, cmap = 'gray');

