import cv2
import numpy as np

for i in range(1, 13):
    file_path = 'images/img (' + str(i) + ').jpg'
    img = cv2.imread(file_path)

    window_width = 800
    window_height = 600

    img = cv2.resize(img, (window_width, window_height))

    cv2.namedWindow("Image")
    position = (0, 0)

    def on_mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global position
            position = (x, y)
            print(position)

    cv2.setMouseCallback("Image", on_mouse_click)

    while True:
        img_copy = img.copy()
        cv2.circle(img_copy, position, 5, (255, 127, 255), 2)

        bgr = np.uint8([[img[position[1], position[0]]]])
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)[0][0]
        cv2.putText(img_copy, f"HSV = {hsv}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 127))

        cv2.imshow("Image", img_copy)

        key = cv2.waitKeyEx(100)
        if key == 27 or key == ord('q'):  # 27 - код клавиши Esc
            break

    cv2.destroyAllWindows()
