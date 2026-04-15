'''
In this file we are going to read the data from the color image
also show the data using matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

lena_color=plt.imread('images/lena_color_512.tif')

print(lena_color.shape) # rows and columns
print(lena_color.size)  # total pixel values

plt.imshow(lena_color)
plt.show()