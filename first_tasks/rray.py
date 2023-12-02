import numpy as np
arr = np.random.randint(0, 20, 20)
mask = arr % 2 == 0
print(arr[mask])