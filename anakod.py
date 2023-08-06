import cv2

cam = cv2.VideoCapture(0)
                    
while cam.isOpened():
    ret, frame = cam.read()

    cv2.imshow('kamera',frame)
    k=cv2.waitKey(1)& 0xFF
    #print (k)
    if k==ord('q'):# q tuşuna basıldığında çık
        break

cam.release()
cv2.destroyAllWindows()
