import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel, threshold_otsu
from skimage.morphology import binary_closing
from skimage.measure import label, regionprops

struct =[[1, 1], 
        [1, 1]]

lama = plt.imread("lama_on_moon.png")
lama = lama.mean(2)

contours = sobel(lama)
tresh = threshold_otsu(contours) * 1.4
print(tresh)

contours[contours < tresh] = 0
contours[contours > 0] = 1

# contours_er = binary_closing(contours, struct)
# labeled_lama = label(contours_er)

regions = regionprops(contours)
max_region = regions[0]
for region in regions:
    if region.area > max_region.area:
        max_region = region

plt.imshow(max_region.image)
plt.colorbar()
plt.show()