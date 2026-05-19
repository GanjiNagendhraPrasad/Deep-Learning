'''
load viola jones maths and give the image to maths
maths will give 2 outcomes
1.no of faces
2. cordinates
'''
import numpy as np
import cv2

old_man=cv2.imread('old_man.jpg')

# load the maths into a varibale
maths=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# give the above image to maths
cordinates, no_of_faces=maths.detectMultiScale2(old_man)

print(no_of_faces)
print(cordinates)

x1 = cordinates[0][0]
y1 = cordinates[0][1]
w = cordinates[0][2]
h = cordinates[0][3]

cv2.rectangle(old_man,(x1,y1),(x1+w,y1+h),(0,0,255),2)

cv2.imshow("single image",old_man)
cv2.waitKey()
cv2.destroyAllWindows()
