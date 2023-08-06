mport cv2


cam = cv2.VideoCapture(0) #0 kendi kameram , 1 ekstra kamera , 2 hazır video
                    
while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.flip(frame,1) #aynalama

    #ret , thresh = cv2.threshold(frame,120,255,cv2.THRESH_BINARY)#krmızı ağırlıklı renklere çevirme
    #ret,thresh2 = cv2.threshold(frame,120,255,cv2.THRESH_BINARY_INV)#mavi ağırlıklı renklere çevirme
    #ret,thresh3 = cv2.threshold(frame,120,255,cv2.THRESH_TRUNC) #ışığı koyultuyor karanlık mod gibi
    #ret,thresh4 = cv2.threshold(frame,120,255,cv2.THRESH_TOZERO)#kırmızı görüntü daha net
    #ret,thresh5 = cv2.threshold(frame,120,255,cv2.THRESH_TOZERO_INV)#mavi görüntü daha net

    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#görüntüyü grileştiriyor


    #cv2.rectangle(frame,(10,20),(150,150),(25,36,98),2) #dikdörtgen ekliyoruz
    #cv2.line(frame,(400,400),(300,300),(10,10,90),2)#çizgi ekiyoruz 
    #cv2.circle(frame,(700,700),100,(80,150,10),2)#daire ekliyoruz
    #cv2.putText(frame,'tuanna', (15,60),cv2.FONT_HERSHEY_DUPLEX,1,(200,0,0),1) #text ekliyoruz

    #cv2.imshow("akincilar",thresh)
    #cv2.imshow('akincilar',thresh2)
    #cv2.imshow('akincilar',thresh3)
    #cv2.imshow('akincilar',thresh4)
    #cv2.imshow('akincilar',thresh5)
    #cv2.imshow('akincilar',gray)

    cv2.imshow('akincilar',frame)

    k = cv2.waitKey(25) & 0xFF
    if k == ord('q'):
        break

    

cam.release()
cv2.destroyAllWindows()
