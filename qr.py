#kendimin internetten bularak yazdığım kod. basit olan.
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('1.png')
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    img = cv2.flip(img,1)
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    cv2.imshow('Result',img)
    cv2.waitKey(1)
