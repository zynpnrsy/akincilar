import cv2
from tespitkismi import tespit
import numpy as np
import datetime



def main():
    kamera = cv2.VideoCapture(0)

    kamera.set(3,640)
    kamera.set(4,480)

    """if (kamera.isOpened() == False): 
        print("KAMERA ACILMADI")"""
    

    t = datetime.datetime.now()
    print("tespite başlanilan saat:" , t.hour ,":", t.minute,":",t.second,":",t.microsecond)

    fourcc = cv2.VideoWriter_fourcc(*"MP4V")
    writer = cv2.VideoWriter("kaydedilen.mp4",fourcc,20,(640,480))
    while kamera.isOpened():
    
        ret, frame = kamera.read()
        frame = cv2.flip(frame,1)
        result  = tespit(frame) #if ile qr veya ucak tespiti kodunu çagirmaliyiz.


        cv2.imshow('QUANTUM UAV DETECTION SYSTEM', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    e = datetime.datetime.now()
    print("tespite tespitin bittiği saat:" , e.hour ,":", e.minute,":",e.second,":",e.microsecond)
    print(e, "süre:", (e-t).total_seconds())

    kamera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
