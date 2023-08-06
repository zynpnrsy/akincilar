import cv2
import numpy as np

cam = cv2.VideoCapture(0)

if(cam.isOpened() == False):
    print("Kamera acilamadi")


cam.set(3,640) #width -kodu 3
cam.set(4,480) #height -kodu4
cam.set(10,100) #parlaklık için -kodu10 -parlaklık derecesi 100




while True:

    success, img = cam.read()
    img = cv2.flip(img,1)

    cv2.rectangle(img,(50,50),(200,200),(0,0,255),2)
    cv2.line(img,(0,0),(50,50),(0,0,255),2)
    cv2.putText(img,"saat",(500,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)


    cv2.imshow("akinci_iha_takimi_[06_08_23]" , img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
