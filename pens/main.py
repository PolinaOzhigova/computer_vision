import numpy as np
import matplotlib.pyplot as plt
import cv2

def detect_pencils(cv2, img, hsv, lower, upper):
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_pencils = 0

    for c in cnts:
        if cv2.contourArea(c) > 500:
            total_pencils += 1
            cv2.drawContours(img, [c], -1, (0, 255, 255), 2)

    return total_pencils

def detect_color(image_path):
    img = cv2.imread(image_path)
    window_width = 800
    window_height = 600
    img = cv2.resize(img, (window_width, window_height))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower1 = (45, 180, 75)
    upper1 = (55, 255, 130) #GREEN

    lower2 = (5, 170, 100)
    upper2 = (10, 230, 190) #ORANGE

    lower3 = (95, 80, 70)
    upper3 = (105, 200, 180) #BLUE

    count = detect_pencils(cv2, img, hsv, lower1, upper1)
    count += detect_pencils(cv2, img, hsv, lower2, upper2)
    count += detect_pencils(cv2, img, hsv, lower3, upper3)
    
    # cv2.imshow("Result", img)
    # cv2.imshow("Mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return count

res = 0
for i in range(1, 13):
    file_path = 'images/img (' + str(i) + ').jpg'
    result = detect_color(file_path)
    res += result
    print(f"Total pencils on the image: {result}")
print()
print(f"RESULT. Total pencils: {res}")