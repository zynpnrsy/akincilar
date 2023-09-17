import cv2
from pyzbar import pyzbar
import datetime
import numpy as np


kamera = cv2.VideoCapture(0)

t = datetime.datetime.now()
print("tespite başlanilan saat:" , t.hour ,":", t.minute,":",t.second,":",t.microsecond)

while True:

    ret, frame = kamera.read()
    frame = cv2.flip(frame,1)

    pksldegerleri = cv2.mean(frame)[0]

    if not ret or frame is None:
        continue

    qrs = pyzbar.decode(frame)
    if qrs:
        for barcode in qrs:
            x, y, w, h = barcode.rect

            points = barcode.polygon

            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (0, 0, 255), 3)
            
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)

            data = barcode.data.decode("utf-8")

            #print(data)

            with open ("data.txt", mode="w") as file:
                file.write("barkod:" + data)

    cv2.imshow('akincilar',frame)
    
    if cv2.waitKey(1) == 27:
        break

print("ort aydinlatma degeri:" , pksldegerleri)

e = datetime.datetime.now()

print(data)
print("tespite tespitin bittiği saat:" , e.hour ,":", e.minute,":",e.second,":",e.microsecond)
print(e, "süre:", (e-t).total_seconds())

kamera.release()
cv2.destroyAllWindows()
