import cv2
print(f"Total in Opencv : {len(dir(cv2))}")
sol = [i for i in dir(cv2) if "EVENT" in i]
print(f"Total : {len(sol)} Functions are available for Mouse Events in OpenCV")


'''
Create a Mouse Event when we click on left button of Mouse we need to get the 
x and y cordinates on top of image 
'''

def sharuk(event,x_cor,y_cor,alpha,beta):
    if event == cv2.EVENT_LBUTTONDOWN:
        text_on_image = str(x_cor)+" "+str(y_cor)
        font_style = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(messi_image,
                    text_on_image,
                    (x_cor,y_cor),
                    font_style,2,(0,0,255),2)
        cv2.imshow("opencv", messi_image)

import numpy as np
messi_image = cv2.imread("images/messi.jpg")

cv2.imshow("opencv" , messi_image)
cv2.setMouseCallback("opencv",sharuk)


cv2.waitKey()
cv2.destroyAllWindows()