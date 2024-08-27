import cv2
import numpy as np

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

        # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        # Define color ranges for each color
        color_ranges = {
            'red': ([0, 50, 50], [10, 255, 255]),          # Red
            'orange': ([11, 50, 50], [25, 255, 255]),      # Orange
            'yellow': ([26, 50, 50], [35, 255, 255]),      # Yellow
            'green': ([36, 50, 50], [70, 255, 255]),       # Green
            'blue': ([101, 50, 50], [130, 255, 255]),     # Blue
            'purple': ([131, 50, 50], [160, 255, 255])    # Purple
        }

        color = None  # Initialize color variable outside the loop

        # Detect the color based on hue value
        for col, (lower, upper) in color_ranges.items():
            if lower[0] <= hue_value <= upper[0]:
                color = col
                break

        # If no color is detected, set to "unknown"
        if color is None:
            color = "unknown"

        # Create masks for each color
        masks = {}
        for col, (lower, upper) in color_ranges.items():
            lower = np.array(lower, dtype=np.uint8)
            upper = np.array(upper, dtype=np.uint8)
            mask = cv2.inRange(hsv_frame, lower, upper)
            masks[col] = mask

        # Display the original image and masks for each color
        cv2.imshow('Original Image', frame)
        for col, mask in masks.items():
            cv2.imshow(col.capitalize() + ' Mask', mask)

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        cv2.putText(frame, color, (cx - 200, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 5)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        print(f"Color: {color}")
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

except Exception as e:
    print("An error occurred:", e)
finally:
    if cap:
        cap.release()  

cv2.destroyAllWindows()
