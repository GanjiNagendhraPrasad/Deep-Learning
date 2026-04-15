'''
In this file we are going to read the data from the grayscale image
using open cv
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

lena_black=cv2.imread('images/lena_gray_512.tif',0)

print(lena_black.shape)
print(lena_black.size)

cv2.imshow('black',lena_black)
cv2.imshow('prasad',lena_black)

cv2.waitKey()
cv2.destroyAllWindows()