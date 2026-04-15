import cv2
import numpy as np


messi_image = cv2.imread("images/messi.jpg")

# messi_image[505 : 623 , 345 : 499] = 0

foot_ball_image = messi_image[505 : 623 , 345 : 499]
messi_image[38 : 156 , 373 : 527] = foot_ball_image


cv2.imshow("original" , messi_image)

cv2.waitKey()
cv2.destroyAllWindows()