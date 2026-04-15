"""
we are going to read the pixel values using imread function in matplotlib
and saving in varibale
know that varibale we are going to give to imshow function which is in opencv
Interview question -> Merc Benz
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

pixel_values_from_mat = plt.imread("images/lena_color_512.tif") # RGB

cv2.imshow("Checking",pixel_values_from_mat[: , : , ::-1]) # RGB -> BGR
cv2.waitKey()
cv2.destroyAllWindows()