import cv2
import time

# Kamera yakalama cihazını başlat
cap = cv2.VideoCapture(0)



fps1  = 25

"""
# FPS değerlerini belirle
fps_camera = 90
fps_capture = 30
"""
# Kamera için FPS değerini al
fps2 = cap.get(cv2.CAP_PROP_FPS)
print("fps2 : ", fps2)

# Kamera yakalanamazsa çık
if not cap.isOpened():
    cap.release()
    exit()

# Zaman ölçümleri için zamanlayıcıları başlat
prev_frame_time = time.time()

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()
    if not ret:
        break

    # Yeni kare zamanını al
    new_frame_time = time.time()
    duration1 = new_frame_time - prev_frame_time
    fps1 = 1 / duration1
    print("fp1 : ", fps1)

    # Her karede belirli bir FPS'e kadar göster
    if duration1 > 1 / fps1:
        prev_frame_time = new_frame_time
        cv2.imshow("Frame", frame)

    # ESC tuşuna basıldığında çık
    key = cv2.waitKey(int(1000 / fps1)) & 0xFF
    if key == 27:
        break

# Kamerayı serbest bırak
cap.release()
cv2.destroyAllWindows()





"""
#BULUNAN İŞE YARAYABİLİR KODLAR
def cozunulukAyarla_1080p():
    kamera.set(3, 1920)
    kamera.set(4, 1080)
# 
    CvVideoWriter *writer = 0;  
int isColor = 1;
int fps     = 25;
int frameW  = 640; // 744 for firewire cameras
int frameH  = 480; // 480 for firewire cameras
#
import cv2

kamera = cv2.VideoCapture(0)

def skalalamaIslemi(cerceve,yukdelikOran): # No-0

    genislik=int((cerceve.shape[1]*yukdelikOran) / 100) # No-1
    yukseklik = int((cerceve.shape[0] * yukdelikOran) / 100) # No-2
    yeniBoyut=(genislik,yukseklik) # No-3
    return cv2.resize(cerceve,yeniBoyut,interpolation=cv2.INTER_AREA) # No-4

while True:
    ret, cerceve = kamera.read()
    oranliCerceve=skalalamaIslemi(cerceve,30) # No-5
    cv2.imshow('Kamera Goruntusu', cerceve)
    cv2.imshow('Kamera Goruntusu (SKALALAMA YAPILMIS GORUNTU)', oranliCerceve) # No-6
    if cv2.waitKey(20) & 0xFF == ord('x'):
        break
kamera.release()
cv2.destroyAllWindows()
#
"""

