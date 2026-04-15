import numpy as np
import cv2
import datetime
import time

black_image = np.zeros((512,512,3) , dtype = np.uint8)

# text_on_image = str(datetime.datetime.now())
# font_style = cv2.FONT_HERSHEY_PLAIN
#
# cv2.putText(black_image,text_on_image,(70,70),font_style,
#         2,(0,255,234),1)
#
# cv2.imshow("Image",black_image)
# cv2.waitKey()

s = 0
t = 70
while True:
    s = s + 1
    text_on_image = str(datetime.datetime.now())
    font_style = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(black_image,text_on_image,(10,t),font_style,
            2,(0,255,234),1)
    cv2.imshow("Image",black_image)
    cv2.waitKey(1000)
    t = t + 20
    if s == 10:
        break



cv2.destroyAllWindows()