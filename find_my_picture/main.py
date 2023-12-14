import cv2
import numpy as np
from skimage import measure
from skimage.measure import label
import matplotlib.pyplot as plt
import time

time_start = time.time()

unique_color_len = 2000 #примерное количество уникальных цветов в мини картиночке

counter = 0

video_file = "output.avi"

capture = cv2.VideoCapture(video_file)
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    
    #для проекрки по юник цвету
    img_slice = frame[350:450, 250:350]
    rgb_image = cv2.cvtColor(img_slice, cv2.COLOR_BGR2RGB)

    unique_colors = np.unique(rgb_image.reshape(-1, rgb_image.shape[2]), axis=0)
    num_unique_colors = len(unique_colors)
    if num_unique_colors > unique_color_len:
        counter += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()

print("Количество кадров нашей прекрасной, замечательной, великолепной и неповторимой природы:", counter)

end_time = time.time()
print(f"Время выполнения: {end_time - time_start} секунд")