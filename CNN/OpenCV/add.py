import cv2
import numpy as np

lena_image = cv2.imread("images/lena_color_512.tif",1)
monkey_image = cv2.imread("images/mandril_color.tif",1)

print(lena_image.shape)
print(monkey_image.shape)

# if you want to add images both images should be same size in rows and columns
# if not there please do resize
# resize(image,(w,h))

#result = cv2.add(lena_image,monkey_image)

result = cv2.addWeighted(lena_image,0.2,monkey_image,0.8,-1)

cv2.imshow("Lena",lena_image)
cv2.imshow("Monkey",monkey_image)
cv2.imshow("adding",result)

cv2.waitKey()
cv2.destroyAllWindows()