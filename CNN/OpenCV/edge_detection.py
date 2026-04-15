import  numpy as  np
import cv2

lena_img=cv2.imread('images/lena_color_512.tif')

edge_img=cv2.Canny(lena_img,211,236)


cv2.imshow('lena',lena_img)
cv2.imshow('edge_img',edge_img)

cv2.waitKey()
cv2.destroyAllWindows()