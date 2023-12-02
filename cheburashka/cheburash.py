import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    cheb = frame

    news = cv2.imread('news.jpg')

    rows, cols, ch = cheb.shape
    pts1 = np.array([[0, 0], [0, rows], [cols, 0], [cols, rows]], dtype="f4")
    pts2 = np.array([[18, 23], [39, 296], [434, 53], [434, 270]], dtype="f4")

    M = cv2.getPerspectiveTransform(pts1, pts2)
    chebuh = cv2.warpPerspective(cheb, M, (news.shape[1], news.shape[0]))

    mask = np.zeros((chebuh.shape[0], chebuh.shape[1]), dtype="uint8")
    mask[chebuh.mean(2) != 0] = 255

    roi = news[:chebuh.shape[1], :chebuh.shape[0]]
    inv_mask = cv2.bitwise_not(mask, mask)
    news_m = cv2.bitwise_and(news, news, mask=inv_mask)

    result = cv2.add(news_m, chebuh)

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", result)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
