import numpy as np
from scipy.ndimage import binary_opening
from skimage.measure import label

struct = np.ones((3, 1))

for i in range(1, 7):
    print(f'file: wires{i}.npy.txt')
    data = np.load(f'wires{i}.npy.txt')
    data = label(binary_opening(data, struct))
    
    num_wires = 0
    num_broken = 0
    
    f = True
    for d in data:
        num = len(set(list(d))) - 1
        if num != 0 and f:
            print(f"Провод {num_wires + 1}: порван на {num} части")
            num_broken += num
            f = False
        if num == 0 and not f:
            num_wires += 1
            f = True
    
    if num_broken == 0:
        print("На изображении нет разорванных проводов.")
    else:
        print(f"Всего {num_broken} разорванных участков провода.\n")

    print("\n")
