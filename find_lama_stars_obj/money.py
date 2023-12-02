import numpy as np
from skimage.measure import label
import matplotlib.pyplot as plt

#arr = np.load("coins.npy.txt")

def neighbours4(y, x):
    return (y, x+1), (y, x-1), (y-1, x), (y+1, x)

def neighbours8(y, x):
    return neighbours4(y, x) + ((y-1, x+1), (y+1, x+1), (y-1, x-1), (y+1, x-1))

def area(labeled, label = 1):
    return np.sum(labeled == label)

def centroid(labeled, label = 1):
    pos = np.where(labeled==label)
    return pos[0].mean(), pos[1].mean()

def get_boundaries(labeled, label=, connectivity=neighbours4):
    pos = np.where(labeled == label)
    bounds = []
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn > labeled.shape[0]-1:
                bounds.append((y, x))
            elif xn < 0 or xn > labeled.shape[1]-1:
                bounds.append((y, x))
            elif labeled[yn, xn] == 0:
                bounds.append((y, x))
    return bounds

LB = np.zeros((16, 16))
LB[4:, :4] = 1

LB[3:10, 8:] = 1
LB[[3, 4, 3],[8, 8, 9]] = 0
LB[[8, 9, 9],[8, 8, 9]] = 0
LB[[3, 4, 3],[-2, -1, -1]] = 0
LB[[9, 8, 9],[-2, -1, -1]] = 0

LB[12:-1, 6:9] = 1

LB = label(LB)

plt.imshow(LB)

for i in range(LB.max()):
    x, y = centroid(LB, i+1)
    plt.scatter(x, y)

plt.show()