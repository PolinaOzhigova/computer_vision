import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
cv2.namedWindow("Camera")
cv2.namedWindow("Debug")

# lower = (90, 150, 120)
# upper = (115, 255, 255) #BLUE

# lower = (0, 205, 170)
# upper = (5, 225, 190) #RED BAD

# lower = (5, 150, 200)
# upper = (30, 255, 255) #ORANGE

lower = (18, 80, 100)
upper = (30, 230, 255) #YELLOW

# lower = (65, 50, 110)
# upper = (85, 170, 200) #GREEN

x0 = None
y0 = None
t = time.perf_counter()
while capture.isOpened():
    t2 = time.perf_counter()
    ret, frame = capture.read()
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.dilate(mask, None, iterations = 2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key = cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
        if x0 and y0:
            s = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
            speed = s / (t2 - t)
            cv2.putText(frame, f"Speed = {speed}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))
        x0 = x
        y0 = y
        t = t2
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 255, 255), -1)

    cv2.imshow("Debug", mask)
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()