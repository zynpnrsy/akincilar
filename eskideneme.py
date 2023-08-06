import cv2
import numpy as np

cam_jetson = cv2.VideoCapture(0)
def jetson(flip=0, width=640, height=480, fps=30):
    #videocapture(yayın yapılacak ipveport gir >> 0-pccam / 1-usbcam)
    cam_jetson = cv2.VideoCapture(0)
    #cam_jetson = flip=0, width=640, height=480, fps=30
    while True:
        ret, goruntu = cam_jetson.read()
        cv2.imshow("gokcen",goruntu)

        if cv2.waitKey(20) & 0xFF == ord("q"):
             break


cam_jetson.release()
cv2.destroyAllWindows()
