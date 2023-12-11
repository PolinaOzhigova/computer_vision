import cv2
import numpy as np
import matplotlib.pyplot as plt
import mss
import pyautogui

# cv2.namedWindow("Screen", cv2.WINDOW_KEEPRATIO)

# def find_dino():
#     image_location = None
#     while image_location is None:
#         try:
#             image_location = pyautogui.locateOnScreen('dino.png')
#             print(f"Изображение найдено. Координаты: {image_location}")
#         except pyautogui.ImageNotFoundException:
#             print("Изображение не найдено.")
#     d_left, d_top, d_width, d_height = image_location
#     point_check = d_left + d_width + 50
#     return point_check


with mss.mss() as sct:
    monitor = {"top": 270, "left": 480, "width": 920, "height": 250}

    while "Screen capturing":
        # img = np.array(sct.grab(sct.monitors[1]))
        img = np.array(sct.grab(monitor))
        
        img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

        # point_check = find_dino()
        # binary_img[point_check[1]][point_check[0]] = 130
        # plt.imshow(binary_img)
        # plt.show()

        # cv2.imshow("Screen", binary_img)
        
        # binary_img[202:204, 150:300] = 130
        # binary_img[160:185, 150:300] = 170
        # plt.imshow(binary_img)
        # plt.show()
        # print(binary_img[180:195, 180:450])
        # print(np.any(binary_img[180:195, 180:450] != 0))

        if np.any(binary_img[180:195, 150:300] == 0):
            pyautogui.press("space")
        elif np.any(binary_img[160:185, 150:250] == 0) and np.all(binary_img[205:207, 150:250] != 0):
            pyautogui.press("down")
        
        
        # Press "q" to quit
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     break