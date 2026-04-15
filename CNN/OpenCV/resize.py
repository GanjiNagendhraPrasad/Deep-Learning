import cv2
import numpy as np
import pandas as pd

a=cv2.imread('images/lena_color_512.tif',1)

print(a.shape) # (r,c,channels)

resized_image = cv2.resize(a,(400,150)) # (w,h)

cv2.imshow("Original",a)
cv2.imshow("resized",resized_image)

cv2.waitKey()
cv2.destroyAllWindows()