import cv2
import numpy as np
from skimage.measure import label, regionprops

image = cv2.imread('balls_and_rects.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

binary = hsv.mean(2) > 0
labeled = label(binary)
regions = regionprops(labeled)

circles_colors = {}
rects_colors = {}
rects = 0
circles = 0
for region in regions:
    color = hsv[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3], 0]
    key = np.max(color[0])
    if len(np.unique(color)) == 1:
        rects += 1
        rects_colors[key] = rects_colors.get(key, 0) + 1
    else:
        circles += 1
        circles_colors[key] = circles_colors.get(key, 0) + 1

print(f"\nAll figures: {np.max(labeled)}")
print(f"Rectangles: {rects}")
print(f"Circles: {circles}\n")

print("{:<10} {:<20} {:<20}".format("Shade", "Rects Colors", "Circles Colors"))
for key in set(rects_colors.keys()).union(circles_colors.keys()):
    print("{:<10} {:<20} {:<20}".format(
        key,
        rects_colors.get(key, ''),
        circles_colors.get(key, '')
    ))