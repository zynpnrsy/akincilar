#tuğçenin bulduğu ilk kod. tespit ettiği karekodları text dosyasında tutuyor.
import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect

        # Sınırlayıcı kutuyu çiz.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Barkod verilerinin kodunu çöz.
        barcode_info = barcode.data.decode("utf-8")
        
        # Barkod verilerini görüntüle.
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x+6, y-6), font, 2.0, (255, 255, 255), 1)
        
        # Barkod verilerini bir dosyaya kaydedin.
        with open("barcode_result.txt", mode="w") as file:
            file.write("Recognized Barcode: " + barcode_info)

    return frame
    
def main():
    camera = cv2.VideoCapture(1)

    while True:
        ret, frame = camera.read()
        if not ret or frame is None:
            continue

        # Barkodları algılamak ve okumak için çerçeveyi işleyin.
        frame = read_barcodes(frame)
        
        # Barkodlu çerçeveyi göster.
        cv2.imshow("Barcode/QR code reader", frame)
        
        # "Esc" tuşuna basılırsa döngüden çıkın.
        if cv2.waitKey(1) == 27:
            break
    
    # Kamerayı serbest bırakın ve pencereyi yok edin.
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

#Kaynakça: https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5


'''12.09.2023 
test1 (17.50): 98cm'ye kadar tespit yapabiliyor.'''
'''15.09.2023
test4 (20.41) 103 cm'ye kadar tespit yapabiliyor.'''
