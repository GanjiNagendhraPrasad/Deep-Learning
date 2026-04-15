import cv2
import numpy as np


mandir_image = cv2.imread("images/mandril_color.tif") # BGR
mandir_hsv_image = cv2.cvtColor(mandir_image,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,50,50])
upper_red = np.array([10, 255, 255])

outcome = cv2.inRange(mandir_hsv_image,lower_red,upper_red)

final_result = cv2.bitwise_and(mandir_image , mandir_image , mask = outcome)

cv2.imshow("original_BGR" , mandir_image)
cv2.imshow("HSV" , mandir_hsv_image)
cv2.imshow("red_on_hsv_image" , outcome)
cv2.imshow("final_result" , final_result)
cv2.waitKey()
cv2.destroyAllWindows()