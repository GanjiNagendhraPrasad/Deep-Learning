import numpy as np
import  cv2

all_images_from_video=cv2.VideoCapture('images/yolo_test.mp4')
driver_name = cv2.VideoWriter_fourcc(*'XVID')

each_image_width = all_images_from_video.get(3) # w
each_image_height = all_images_from_video.get(4) # h

output_area = cv2.VideoWriter("images/traffic.avi",driver_name,20.0,(int(each_image_width),int(each_image_height)))


c=0
while True:
    status,pixel_value=all_images_from_video.read()
    c=c+1
    if status==True:
        text_on_image='frame : '+str(c)
        font_style=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(pixel_value,text_on_image,(50,50),font_style,2,(0,0,255),2)
        cv2.imshow('images',pixel_value)
        output_area.write(pixel_value)
        #cv2.imwrite('images/all_im/'+str(c)+'.jpg',pixel_value)
        if cv2.waitKey(25) % 0xFF==ord('q'):
            break
    else:
        break


all_images_from_video.release()
cv2.destroyAllWindows()