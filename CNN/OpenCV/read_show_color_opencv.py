'''
In this file we are going to read the data from the color image
using open cv
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

lena_color=cv2.imread('images/lena_color_512.tif',1)

print(lena_color.shape)
print(lena_color.size)
print(lena_color)

cv2.imshow('color',lena_color)
cv2.imshow('prasad',lena_color)

cv2.waitKey()
cv2.destroyAllWindows()