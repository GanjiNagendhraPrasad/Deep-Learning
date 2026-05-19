'''
load viola jones maths and give the image to maths
maths will give 2 outcomes
1.no of faces
2. cordinates
'''
import numpy as np
import cv2

#old_man=cv2.imread('faces.jpg')
old_man=cv2.imread('1.jpg')

# load the maths into a varibale
maths=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# give the above image to maths
cordinates, no_of_faces=maths.detectMultiScale2(old_man)

print(f"number of faces : {no_of_faces}")
print(f"==========cordinates=========")
print(cordinates)

for i in range(len(no_of_faces)):
    values = cordinates[i]
    x1,y1,w,h = values[0],values[1],values[2],values[3]
    cv2.rectangle(old_man,(x1,y1),(x1+w,y1+h),(0,255,0),2)

cv2.imshow("single image",old_man)
cv2.waitKey()
cv2.destroyAllWindows()
