#tuğçenin attığı 3. kod. 
import cv2

# Kamera ayarları
camera_id = 1       # Kameranın ID numarası
delay = 1        # Her frame arasındaki gecikme süresi (ms)

# Pencere adı
window_name = 'OpenCV QR Code'

# QR kodu tanıma nesnesi oluştur
qcd = cv2.QRCodeDetector()

# Kamera yakalama nesnesi oluştur
cap = cv2.VideoCapture(camera_id)

while True:
    # Kameradan bir frame yakala
    ret, frame = cap.read()

    if ret:
        # QR kodunu tespit et ve çöz
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        
        if ret_qr:
            # QR kodu tespit edildiyse
            for s, p in zip(decoded_info, points):
                if s:
                    # QR kodu başarıyla çözüldüyse
                    print(s)
                    color = (0, 255, 0)  # Yeşil renk
                else:
                    # QR kodu çözülemediyse
                    color = (0, 0, 255)  # Kırmızı renk
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        
        # Frame'i ekranda göster
        cv2.imshow(window_name, frame)

    # 'q' tuşuna basılırsa döngüyü sonlandır
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Pencereyi kapat
cv2.destroyWindow(window_name)


'''12.09.2023
test2(20.41) : yerden 68cm yüksekliğe kadar okuyor'''
