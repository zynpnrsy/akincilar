import cv2
import numpy as np


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR CODE: CAMERA COULD NOT OPEN")
    exit()

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
   # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)   
    
     # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

     # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    # Purple color
    low_purple = np.array([130, 50, 50])
    high_purple = np.array([170, 255, 255])
    purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)
    purple = cv2.bitwise_and(frame, frame, mask=purple_mask)

    # Brown color (combining red and green)
    low_brown = np.array([0, 50, 50])
    high_brown = np.array([30, 255, 255])
    brown_mask1 = cv2.inRange(hsv_frame, low_brown, high_brown)

    low_brown = np.array([30, 50, 50])
    high_brown = np.array([90, 255, 255])
    brown_mask2 = cv2.inRange(hsv_frame, low_brown, high_brown)

    brown_mask = cv2.bitwise_or(brown_mask1, brown_mask2)
    brown = cv2.bitwise_and(frame, frame, mask=brown_mask)

    # Yellow color
    low_yellow = np.array([20, 100, 100])
    high_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    # Orange color
    low_orange = np.array([5, 100, 100])
    high_orange = np.array([15, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    # White color
    low_white = np.array([0, 0, 200])
    high_white = np.array([180, 30, 255])
    white_mask = cv2.inRange(hsv_frame, low_white, high_white)
    white = cv2.bitwise_and(frame, frame, mask=white_mask)

    # Black color
    low_black = np.array([0, 0, 0])
    high_black = np.array([180, 255, 30])
    black_mask = cv2.inRange(hsv_frame, low_black, high_black)
    black = cv2.bitwise_and(frame, frame, mask=black_mask)

        
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Orange", orange)
    cv2.imshow("Yellow", yellow)
    cv2.imshow("Brown", brown)
    cv2.imshow("White", white )
    #cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    
cap.release()
cv2.destroyAllWindows()

