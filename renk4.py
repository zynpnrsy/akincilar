
#siyah-beyaz renkleri kodda yok.kahverengi algilamada ise sorun yasaniyor. 
#Diger renkler ise belirgin tanitilmali,ton farklarinda hata verebilir.

import cv2
import numpy as np

#kamera acma kodu, 1-pc_cam ,0-usb_cam 
cap = cv2.VideoCapture(1)

#kamera acildi mi kontrolu 
if not cap.isOpened():
    print("ERROR CODE: CAMERA ERROR")
    exit()

#width-height hesaplama
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    ret, frame = cap.read()
   
#frame ok mu kontrolu 
    
    if not ret:
        print("ERROR CODE: FRAME ERROR")
        break
    
        #cv2-renk modulu
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape


    #hue valueların rangeleri
    color_ranges = {
            
        'yellow': ([22, 100, 100], [38, 255, 255]),  # Yellow
        'red': ([0, 100, 100], [10, 255, 255]),      # Red
        'orange': ([11, 100, 100], [20, 255, 255]),  # Orange
        'purple': ([130, 50, 50], [160, 255, 255]),  # Purple
        'brown': ([7, 50, 50], [20, 255, 255]),      # Brown
        'blue': ([90, 50, 50], [130, 255, 255]),     # Blue
        'green': ([36, 50, 50], [86, 255, 255])      # Green
    }

    hue_channel = hsv_frame[:, :, 0]

    #merkez hesaplama
    cx = int(width / 2)
    cy = int(height / 2)

    #merkez almak icin 0
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "UNDEFINED"

    #hue value degerleri
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 160:
        color = "PURPLE"
    elif hue_value < 20:
        color = "BROWN"

    print("Color:", color)

    #renkleri ekrana yazdirmak icin
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    #renkleri ekrana yazdirmak icin
    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 20, (25, 25, 25), 3)
# en bastaki 20 dairenin capi # sondaki 3 kalinlik # ortadaki 3lu degerler renkler, 25=siyah 

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:      #esc = ending tusu
        break

cap.release()
cv2.destroyAllWindows()
