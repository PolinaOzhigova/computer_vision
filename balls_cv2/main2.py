import cv2

capture = cv2.VideoCapture(0)
cv2.namedWindow("Camera")
cv2.namedWindow("Debug")

roi = None
while capture.isOpened():
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("b"):
        r = cv2.selectROI("ROI selection", gray)
        roi = gray[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
        cv2.imshow("Debug", roi)
        cv2.destroyWindow("ROI selection")

    if roi is not None:
        result = cv2.matchTemplate(gray, roi, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + roi.shape[1], top_left[1] + roi.shape[0])
        cv2.rectangle(result, top_left, bottom_right, 255, 2)
        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 255), 2)
        cv2.imshow("Debug", result)

    cv2.imshow("Camera", frame)

capture.release()
cv2.destroyAllWindows