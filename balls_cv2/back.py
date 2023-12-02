import cv2
import time

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
#cam.set(cv2.CAP_PROP_EXPOSURE, -1)

cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
#cv2.namedWindow("Background", cv2.WINDOW_KEEPRATIO)

background = None
t_prev = time.perf_counter()
while cam.isOpened():
    t_curr = time.perf_counter()
    print(t_curr - t_prev)
    t_prev = t_curr
    
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('b'):
        background = gray.copy()

    if background is not None:
        delta = cv2.absdiff(background, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=5)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            area = cv2.contourArea(c)
            if area > 5000:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Debug", thresh)

    cv2.imshow("Camera", frame)

cam.release()
cv2.destroyAllWindows()