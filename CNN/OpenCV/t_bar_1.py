import numpy as np
import cv2

def fun(x):
    pass

cv2.namedWindow('tbar')
cv2.createTrackbar('Low_value','tbar',0,255,fun)
cv2.createTrackbar('High_value','tbar',0,255,fun)

while True:
    image = cv2.imread('images/lena_color_512.tif')
    low_value=cv2.getTrackbarPos('Low_value','tbar')
    high_value=cv2.getTrackbarPos('High_value','tbar')
    # text_on_image=str(low_value)+'        '+str(high_value)
    # font_style=cv2.FONT_HERSHEY_PLAIN
    # cv2.putText(image,text_on_image,(150,250),font_style,2,(0,255,0),2)
    edge_image=cv2.Canny(image,low_value,high_value)
    cv2.imshow('tbar',edge_image)
    #cv2.imshow('tbar',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()