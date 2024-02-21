from pyzbar import pyzbar
import cv2
import numpy as np




def tespit(frame):
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
            with open ("data.txt", mode="w") as file:
                file.write("barkod:" + data) 
