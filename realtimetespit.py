import cv2
import numpy as np
from torch import cuda
import torch
import time
# YOLOv5 modelini yükle
model = torch.hub.load('ultralytics/yolov5', 'custom', path="best3.pt", force_reload=True)
device = torch.device('cuda' if cuda.is_available() else 'cpu')

# Metin tespiti için önceden eğitilmiş ağırlıkları yükle
text_detection_model = torch.hub.load('ultralytics/yolov5', 'custom', path="harf2.pt", force_reload=True)

# Video akışını aç
video_capture = cv2.VideoCapture(0)

fps_camera = 90
fps_capture = 30

fps2 = video_capture.get(cv2.CAP_PROP_FPS)
print("fps2 : ", fps2)
prev_frame_time = time.time()

while True:
    # Kareden oku
    ret, frame = video_capture.read()
    
    # YOLOv5 modeli için uygun formata getir
    frame = [frame]

    # Tespit yap
    results = model(frame)
    results2 = text_detection_model(frame)

    # Tespit sonuçlarını al
    shapes = results.pandas().xyxy[0]
    letter = results2.pandas().xyxy[0]

    # Tespit edilen şekilleri çiz
    for index, row in shapes.iterrows():
        label = int(row['class'])
        bbox = [int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])]
        text = shapes.to_string(index = False)
        #print = ('Detected shape:', text)
        
        print('Detected shape:', row['name'])
        
        # Tespit edilen şekli çizmek için gerekli koordinatları alın
        xmin, ymin, xmax, ymax = bbox
        cv2.rectangle(frame[0], (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame[0], row['name'], (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    for index, row in letter.iterrows():
        label = int(row['class'])
        bbox = [int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])]
        text2=letter.to_string(index=False)

        
        print('Detected letter:', text2)

        xmin, ymin, xmax, ymax = bbox
        cv2.rectangle(frame[0], (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame[0], row['name'], (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)




        



    # Renkler için işlemler
    hsv_frame = cv2.cvtColor(frame[0], cv2.COLOR_BGR2HSV)
    height, width, _ = frame[0].shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "UNDEFINED"

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


    pixel_center_bgr = frame[0][cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame[0], (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame[0], color, (cx - 200, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (b, g, r), 5)
    cv2.circle(frame[0], (cx, cy), 20, (25, 25, 25), 3)

    new_frame_time = time.time()
    duration1 = new_frame_time - prev_frame_time
    fps = 1 / duration1
    print("fps : ", fps)

    # Her karede belirli bir FPS'e kadar göster
    if duration1 > 1 / fps_capture:
        prev_frame_time = new_frame_time
        
        cv2.imshow("Frame", frame[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video akışını kapat
video_capture.release()
cv2.destroyAllWindows()
