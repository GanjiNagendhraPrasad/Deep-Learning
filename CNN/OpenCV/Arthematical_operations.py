'''
In this file we are going to apply

1. rectangle
2. line
3. arrowed line
4. circle
5. puttext

on the image
'''
import numpy as np
import cv2

image = cv2.imread("images/old.jpg")
print(image.shape)

# rectangle
#cv2.rectangle(image,(15,300),(660,580),(0,0,255),2)

# line
#cv2.line(image,(15,300),(660,580),(0,255,0),2)

#arrowedLine
#cv2.arrowedLine(image,(15,300),(660,580),(0,0,255),2)

# circle
#cv2.circle(image,(350,447) , 150 , (255,0,0,),2)

text_on_image = "wilson"
font_style = cv2.FONT_HERSHEY_PLAIN
cv2.putText(image,text_on_image,(60,100),font_style,8,(0,255,239),2)


cv2.imshow("Old_Man_Image",image)
cv2.waitKey()
cv2.destroyAllWindows()