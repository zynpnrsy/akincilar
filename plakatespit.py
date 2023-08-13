import cv2


arabaveri = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)
cam = cv2.VideoCapture(1) #0 kendi kameram , 1 ekstra kamera , 2 hazır video
width = int(cam.get(3))
height = int(cam.get(4))  
count = 0
                 
while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    grileme = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    averi = arabaveri.detectMultiScale(grileme,1.1,4)

    for (x,y,w,h) in averi:
        area = w*h
        if area >minArea:
            cv2.rectangle(frame,(x, y),(x + w, y - h), (255,0,0),2)
            cv2.putText(frame,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            frameRoi = frame[y:y+h,x:x+w]
            cv2.imshow('akincilar',frameRoi)
    cv2.imshow("akincilar",frame)


    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        cv2.imwrite("NoPlate_"+str(count)+".jpg",frameRoi)
        cv2.rectangle(frame,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",frame)
        cv2.waitKey(500)
        count +=1
        break

    

cam.release()
cv2.destroyAllWindows()
