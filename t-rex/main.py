import cv2
import numpy as np
import matplotlib.pyplot as plt
import mss
import pyautogui
import time

def find_dino():
    image_location = None
    while image_location is None:
        try:
            image_location = pyautogui.locateOnScreen('dino.png')
            print(f"Изображение найдено. Координаты: {image_location}")
            pyautogui.press("space")
        except pyautogui.ImageNotFoundException:
            print("Изображение не найдено.")
    d_left, d_top, d_width, d_height = image_location
    point_check = (d_left + d_width + 50, d_top)
    return point_check, d_left, d_width

point_check, d_left, d_width = find_dino()

with mss.mss() as sct:

    while "Screen capturing":

        img = np.array(sct.grab(sct.monitors[1]))
        
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        # binary_img[point_check[1]:point_check[1]+5, point_check[0]:point_check[0]+i] = 170
        # plt.imshow(binary_img)
        # plt.show()

        if np.any(binary_img[point_check[1]:point_check[1]+30, point_check[0]:point_check[0]+150] == 0):
            pyautogui.press("space")

cv2.destroyAllWindows()