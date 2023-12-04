import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

x, y = [], []

for i in range(100):
    file_path = f'out/h_{i}.npy'
    data = np.load(file_path)

    labeled = label(data)
    regions = sorted(regionprops(labeled), key=lambda region: region.area)

    for j in range(3):
        x.append(regions[j].centroid[0])
        y.append(regions[j].centroid[1])

plt.plot(x[::3], y[::3], label='1 шарик')
plt.plot(x[1::3], y[1::3], label='2 шарик')
plt.plot(x[2::3], y[2::3], label='3 шарик')
plt.legend()
plt.show()