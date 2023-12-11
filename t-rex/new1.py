import cv2
import numpy as np
import mss
import pyautogui

with mss.mss() as sct:
    monitor = {"top": 270, "left": 480, "width": 920, "height": 250}

    while "Screen capturing":
        img = np.array(sct.grab(monitor))
        # img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        # gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        # _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        binary_img = hsv.mean(2) > 0

        point_check = (500, 190)
        square_size = 30
        top_left = (point_check[0] - square_size // 2, point_check[1] - square_size // 2)
        bottom_right = (point_check[0] + square_size // 2, point_check[1] + square_size // 2)

        region_of_interest = (binary_img * 255).astype(np.uint8)

        cv2.imshow("Region of Interest", region_of_interest)
    
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break