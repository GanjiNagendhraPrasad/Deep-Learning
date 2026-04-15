'''
In this file we are going to read the data from the gray scale image
also show the data using matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

lena_black=plt.imread('images/lena_gray_512.tif')

print(lena_black.shape) # rows and columns
print(lena_black.size)  # total pixel values

plt.imshow(lena_black,cmap='gray')
plt.show()