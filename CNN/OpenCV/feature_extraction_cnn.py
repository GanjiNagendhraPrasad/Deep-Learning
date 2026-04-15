import cv2
import numpy as np

image=cv2.imread('images/messi.jpg')

kernel_filter=np.array([[0,1,0],[1,-4,1],[0,1,0]])

r=cv2.filter2D(image,-1,kernel=kernel_filter)

cv2.imshow('image',image)
cv2.imshow('kernel',r)

cv2.waitKey()
cv2.destroyAllWindows()