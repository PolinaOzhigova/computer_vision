import cv2
import numpy as np
import matplotlib.pyplot as plt

#Кол-во юник оттенков на мини картинке
image = cv2.imread('ozhigova.png')

plt.imshow((image[350:450, 250:350]))
plt.show()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
unique_colors = np.unique(rgb_image.reshape(-1, rgb_image.shape[2]), axis=0)
num_unique_colors = len(unique_colors)
print(num_unique_colors)