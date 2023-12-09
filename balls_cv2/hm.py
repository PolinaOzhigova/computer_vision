import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
capture.set(cv2.CAP_PROP_EXPOSURE, -6)
cv2.namedWindow("Camera")
# cv2.namedWindow("Debug")

lower4 = (90, 150, 120)
upper4 = (115, 255, 255) #BLUE

# lower = (0, 205, 170)
# upper = (5, 225, 190) #RED BAD

lower2 = (0, 150, 200)
upper2 = (10, 255, 255) #ORANGE

lower1 = (23, 80, 100)
upper1 = (35, 230, 255) #YELLOW

lower3 = (65, 50, 110)
upper3 = (85, 170, 200) #GREEN

def centers(cv2, hsv, lower, upper):
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.dilate(mask, None, iterations = 2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key = cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
        return center

while capture.isOpened():
    ret, frame = capture.read()
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    cv2.putText(frame, f"Show Yellow Orange Green (Blue)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    c1 = centers(cv2, hsv, lower1, upper1)
    c2 = centers(cv2, hsv, lower2, upper2)
    c3 = centers(cv2, hsv, lower3, upper3)
    c4 = centers(cv2, hsv, lower4, upper4)
    cv2.putText(frame, f"{c1, c2, c3, c4}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))
    y_max = frame.shape[0] #480
    x_max = frame.shape[1] #640
    if(c1 != None and c2 != None and c3 != None):
        if(c1[0] < c2[0] and c1[1] < c2[1] and c2[0] < c3[0] and c2[1] < c3[1]):
            cv2.putText(frame, f"DONE!", (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))
        if(c4 != None):
            if(c1[1] < c2[1] and c3[1] < c4[1]):
                cv2.putText(frame, f"DONE2!", (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))

    # cv2.imshow("Debug", mask)
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()