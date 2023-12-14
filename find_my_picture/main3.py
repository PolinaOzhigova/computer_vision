import cv2
import numpy as np
from skimage import measure
from skimage.measure import label
import matplotlib.pyplot as plt
import time

time_start = time.time()

counter = 0

video_file = "output.avi"

capture = cv2.VideoCapture(video_file)
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    #для проекрки по количеству объектов
    img = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    labeled = label(binary_img)

    if np.max(labeled) == 24:
        counter += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()

print("Количество кадров нашей прекрасной, замечательной, великолепной и неповторимой природы:", counter)

end_time = time.time()
print(f"\nВремя выполнения: {end_time - time_start} секунд")