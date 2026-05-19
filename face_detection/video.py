import numpy as np
import cv2


all_images = cv2.VideoCapture("test_video1.mp4")
w = all_images.get(3) # w
h = all_images.get(4) # h

driver = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output_face_detection.avi",driver,20.0,(int(w),int(h)))


maths = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    status,pixel_values = all_images.read()
    if status == True:
        cordinates,no_of_faces = maths.detectMultiScale2(pixel_values)
        for i in range(len(no_of_faces)):
            values = cordinates[i]
            x1, y1, w, h = values[0], values[1], values[2], values[3]
            cv2.rectangle(pixel_values, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
        output.write(pixel_values)

        cv2.imshow("current",pixel_values)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

all_images.release()
cv2.destroyAllWindows()