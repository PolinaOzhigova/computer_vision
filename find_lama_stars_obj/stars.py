import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion, binary_closing, binary_opening
from skimage.measure import label


struct =  [[[1, 0, 0, 0, 1], 
            [0, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1]],
        
            [[0, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0], 
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]]]

data = np.load('stars.npy')

plt.imshow(data)
plt.show()

labeled = label(data)

print('TOTAL: ', labeled.max())

res = 0
for x in range(1, labeled.max() + 1):
    star = np.zeros_like(data)
    star[labeled == x] = 1
    for y in range(len(struct)):
        get_star = binary_erosion(star, struct[y])
        labeled2 = label(get_star)
        if labeled2.max() != 0:
            res += 1

print('STARS: ', res)