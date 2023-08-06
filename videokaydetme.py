import cv2


kamera= cv2.VideoCapture(0)
width = int(kamera.get(3))
height = int(kamera.get(4))

fourcc = cv2.VideoWriter_fourcc(*"MP4V")
writer = cv2.VideoWriter("kaydedilen.mp4",fourcc,20,(width,height))

while True:
    ret, frame = kamera.read()
    frame = cv2.flip(frame,1)
    writer.write(frame)

    cv2.imshow("akincilar",frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


kamera.release()
writer.release()
cv2.destroyAllWindows()
