import cv2
from pyzbar import pyzbar


kamera = cv2.VideoCapture(1)

while True:
    ret, frame = kamera.read()
    frame = cv2.flip(frame,1)
    if not ret or frame is None:
        continue
    qrs = pyzbar.decode(frame)
    for barcode in qrs:
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255),2)
            data = barcode.data.decode("utf-8")
            print(data)
            with open ("data.txt", mode="w") as file:
                file.write("barkod:" + data)
        
    cv2.imshow('akincilar',frame)

    if cv2.waitKey(1) == 27:
        break
    
kamera.release()
cv2.destroyAllWindows()
