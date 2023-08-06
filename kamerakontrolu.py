import cv2

def check_available_cameras(num_cameras=4):
    for i in range(num_cameras):
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            print(f"Camera {i} not found or can't be opened!")
        else:
            print(f"Camera {i} is available!")
            cap.release()

if __name__ == "__main__":
    check_available_cameras()
