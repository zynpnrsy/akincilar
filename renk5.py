import cv2
import numpy as np

# Load image
cam = cv2.VideoCapture(1)

if not cam.isOpened():
    print("ERROR CODE: CAMERA ERROR")
    print("Continuing execution...")

while True:
    # Capture frame
    ret, frame = cam.read()

    # Break the loop if the frame is not captured successfully
    if not ret:
        print("ERROR CODE: FRAME CAPTURE ERROR")
        break

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours of black and white regions
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on original image
    image_with_contours = frame.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Display results
    cv2.imshow('Original Image', frame)
    cv2.imshow('Binary Image', binary)
    cv2.imshow('Image with Contours', image_with_contours)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()