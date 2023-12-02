import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def neighbours4(y, x):
    return (y, x+1), (y, x-1), (y-1, x), (y+1, x)

def neighbours8(y, x):
     return neighbours4(y, x) + ((y-1, x+1), (y+1, x+1), (y-1, x-1), (y+1, x-1))

def get_boundaries(labeled, label=1, connectivity=neighbours4):
    pos = np.where(labeled == label)
    bounds = []
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn > labeled.shape[0]-1:
                bounds.append((y, x))
                break
            elif xn < 0 or xn > labeled.shape[1]-1: 
                bounds.append((y, x))
                break
            elif labeled[yn, xn] == 0:
                bounds.append((y, x))
                break
    return bounds

def made_chain(labeled):
    result = []
    bounds = get_boundaries(labeled)

    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    y, x = bounds[0]

    for _ in range(len(bounds)):
        for i, (dy, dx) in enumerate(directions):
            next_y, next_x = y + dy, x + dx
            if (next_y, next_x) in bounds:
                result.append(i)
                bounds.remove((next_y, next_x))
                y, x = next_y, next_x
                break

    return result

def work_with_file(data):
    labeled = label(data)
    a = np.max(labeled)

    result = []
    for i in range(1, a+1):
        result.append(made_chain(labeled))
    print()
    print("RESULT: ", result)
    return result

def check_equals(figures):
    first = figures[0]
    f = False
    for i in figures:
        if f == False:
            f = True
            continue
        if first == i:
            print(True)
    return

img = np.load('similar.npy')
figures = work_with_file(img)
check_equals(figures)

plt.imshow(img)
plt.show()

data = np.array([[0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0]])
work_with_file(data)

print("GOOD RESULT: 0 2 2 4 6 6")

circle = np.array([[0, 0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0, 0], 
                [0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0], 
                [0, 0, 1, 1, 0, 0]])
work_with_file(circle)

print("GOOD RESULT: 0 1 2 3 4 5 6 7")