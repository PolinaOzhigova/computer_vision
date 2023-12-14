import cv2
import numpy as np
from skimage import measure
from skimage.measure import label
import matplotlib.pyplot as plt
import time

time_start = time.time()

target_color = np.array([191, 225, 156])

counter = 0

video_file = "output.avi"

capture = cv2.VideoCapture(video_file)
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    
    img_slice = frame[110:120, 95:102]
    rgb_image = cv2.cvtColor(img_slice, cv2.COLOR_BGR2RGB)

    if np.any(np.all(rgb_image == target_color, axis=-1)):
        counter += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()

print("Количество кадров нашей прекрасной, замечательной, великолепной и неповторимой природы:", counter)

end_time = time.time()
print(f"\nВремя выполнения: {end_time - time_start} секунд")