import cv2
import numpy as np
import matplotlib.pyplot as plt
import mss
import pyautogui
import time

# time_sleep = 0.18

def find_c():
    try:
        image_location = pyautogui.locateOnScreen('c.png')
        return True
    except pyautogui.ImageNotFoundException:
        return False

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
# time_sleep = 0.1
# print(point_check)
# f = False

i = 150

with mss.mss() as sct:
    last_space_press_time = time.time()
    # count = 0

    while "Screen capturing":
        current_time = time.time()
        f = False
        # print(current_time - last_space_press_time)
        if current_time - last_space_press_time >= 20 and f == False:
            f = True
            last_space_press_time = current_time
        if current_time - last_space_press_time >= 5 and f == True:
            # time_sleep -= 0.005
            i += 1
            # print(i)
            # count += current_time - last_space_press_time
            last_space_press_time = current_time
        # if current_time - last_space_press_time >= 2 and count >=50:
        #     time_sleep -= 0.008
        #     last_space_press_time = current_time
        #     i += 5

        img = np.array(sct.grab(sct.monitors[1]))
        
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        # binary_img[point_check[1]:point_check[1]+5, point_check[0]:point_check[0]+i] = 170
        # plt.imshow(binary_img)
        # plt.show()

        if(find_c()):
            i -= 20
        if np.any(binary_img[point_check[1]:point_check[1]+30, point_check[0]:point_check[0]+i] == 0):
            pyautogui.press("space")
            time.sleep(0.001)
            # if (time_sleep > 0):
            #     time.sleep(time_sleep)
            # if not np.all(binary_img[point_check[1]+20:point_check[1]+25, d_left:d_left+d_width+150] == 1):
            #     pyautogui.press('down')
        if np.any(binary_img[point_check[1]:point_check[1]+30, point_check[0]:point_check[0]+i-10] == 0) and np.all(binary_img[point_check[1]+25:point_check[1]+40, d_left:d_left+d_width+i-120] == 255):
            pyautogui.PAUSE = 0
            pyautogui.keyDown('down')
            time.sleep(0.002)
            pyautogui.keyUp('down')
            # pyautogui.press('down')
            pyautogui.PAUSE = 0.1
            print("down")

cv2.destroyAllWindows()