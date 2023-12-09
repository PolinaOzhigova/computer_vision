import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion
from skimage.measure import label, regionprops
from skimage.draw import disk
import cv2

image = plt.imread('balls_and_rects.png')
print(image.shape)

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

#colors = np.unique(hsv[:, :, 0])
binary = image.mean(2) > 0
labeled = label(binary)
# print("max(labeled) ", np.max(labeled))

regions = regionprops(labeled)
colors = []
h = hsv[:, :, 0]
for region in regions:
    pixels = h[region.coords]
    r = h[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
    colors.extend(np.unique(r)[1:])
print("number of bulls ", len(colors))

clusters = []
while colors:
    color1 = colors.pop(0)
    clusters.append([color1])
    for color2 in colors.copy():
        if abs(color1 - color2) < 5:
            clusters[-1].append(color2)
            colors.pop(colors.index(color2))

for cluster in clusters:
    print(len(cluster))

# plt.plot(colors, "0")
# plt.imshow(h)
# plt.show()