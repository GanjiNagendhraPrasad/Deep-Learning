import numpy as np
import cv2

def fun(x):
    pass

cv2.namedWindow('tbar')
cv2.createTrackbar("l-h","tbar",0,255,fun)
cv2.createTrackbar("l-s","tbar",0,255,fun)
cv2.createTrackbar("l-v","tbar",0,255,fun)
cv2.createTrackbar("h-h","tbar",255,255,fun)
cv2.createTrackbar("h-s","tbar",255,255,fun)
cv2.createTrackbar("h-v","tbar",255,255,fun)

while True:
    #image = cv2.imread("images/lena_color_512.tif")
    image = cv2.imread("images/mandril_color.tif")
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    low_hue = cv2.getTrackbarPos("l-h", "tbar")
    low_sat = cv2.getTrackbarPos("l-s", "tbar")
    low_val = cv2.getTrackbarPos("l-v", "tbar")
    high_hue = cv2.getTrackbarPos("h-h", "tbar")
    high_sat = cv2.getTrackbarPos("h-s", "tbar")
    high_val = cv2.getTrackbarPos("h-v", "tbar")

    lower_red = np.array([low_hue, low_sat, low_val])
    upper_red = np.array([high_hue, high_sat, high_val])

    outcome = cv2.inRange(image, lower_red, upper_red)

    final_result = cv2.bitwise_and(image, image, mask=outcome)

    cv2.imshow("tbar", final_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()