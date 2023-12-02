import cv2
import numpy as np

capture = cv2.VideoCapture(0)
cv2.namedWindow("Camera")
cv2.namedWindow("Debug")

position = (0, 0)
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        position = (x, y)
        print(position)

cv2.setMouseCallback("Camera", on_mouse_click)

while capture.isOpened():
    ret, frame = capture.read()
    cv2.circle(frame, position, 5, (255, 127, 255), 2)

    bgr = np.uint8([[frame[position[1], position[0]]]])
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)[0][0]
    cv2.putText(frame, f"HSV = {hsv}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()