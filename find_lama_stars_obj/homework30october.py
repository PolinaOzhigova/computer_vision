import numpy as np
from scipy.ndimage import binary_dilation, binary_erosion, binary_closing, binary_opening
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

struct = {
    "rectangle":[[1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1]],

    "left":[[1,1,1,1],
            [1,1,1,1],
            [0,0,1,1],
            [0,0,1,1],
            [1,1,1,1],
            [1,1,1,1]],

    "right":[[1,1,1,1],
            [1,1,1,1],
            [1,1,0,0],
            [1,1,0,0],
            [1,1,1,1],
            [1,1,1,1]],

    "up": [[1,1,0,0,1,1],
            [1,1,0,0,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]],

    "down": [[1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,0,0,1,1],
            [1,1,0,0,1,1]]
}

data = np.load('ps.npy.txt')
# plt.imshow(data)
# plt.show()

labeled = label(data)

print(f"Общее количество объектов: {labeled.max()}")

counts = {}
for key, value in struct.items():
    get_data = label(binary_erosion(data, value)).max()
    if key not in counts:
        counts[key] = 0
    counts[key] = get_data
counts["up"] -= counts["rectangle"]
counts["down"] -= counts["rectangle"]
print(counts)