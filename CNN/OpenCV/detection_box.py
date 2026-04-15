import numpy as np
import cv2

image = cv2.imread("images/cameraman.tif",1)
print(image.shape)

# rectangle
cv2.rectangle(image,(50,50),(270,510),(0,0,255),2)

text_on_image = "cameraman"
font_style=cv2.FONT_HERSHEY_PLAIN

cv2.putText(image,text_on_image,(50,40),font_style,2,(0,0,255),2)

cv2.imshow("Old_Man_Image",image)
cv2.waitKey()
cv2.destroyAllWindows()
