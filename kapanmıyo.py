import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(300,300)
cam.set(400,400)



cv2.startWindowThread()

while True:
    ret, img = cam.read()
    cv2.imshow("zp" , img)

    if cv2.waitKey(0) & 0xFF == ('q'):
        break

    

cam.release()

cv2.destroyAllWindows()
cv2.waitKey(1)