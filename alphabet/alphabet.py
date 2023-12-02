import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def filling_factor(region):
    return region.image.mean()


def recognize(region):
    if filling_factor(region) == 1:
        return "-"
    euler = region.euler_number
    match euler:
        case -1:  # B or 8
            if 1 in region.image.mean(0):
                return "B"
            return "8"
        case 0:  # A or 0
            tmp = region.image.copy()
            tmp[-1, :] = 1
            tmp_regions = regionprops(label(tmp))
            if tmp_regions[0].euler_number == -1:
                return "A"
            return "0"
        case _:  # 1 W X / *
            if 1 in region.image.mean(0):
                return "1"
            tmp = region.image.copy()
            tmp[-1, :] = 1
            tmp[0, :] = 1
            tmp_regions = regionprops(label(tmp))
            euler = tmp_regions[0].euler_number
            if euler == -1:
                return "X"
            elif euler == -2:
                return "W"
            if region.eccentricity > 0.5:
                return "/"
            return "*"
    return "?"

img = plt.imread('alphabet.png')

binary = img.mean(2)
binary[binary>0] = 1
labeled = label(binary)
print(labeled.max())

regions = regionprops(labeled)

counts = {}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1
print(counts)
print(round(1.0 - counts.get("?", 0)/labeled.max(), 4)*100, "%")

#mean(0) сложит построчно и поделит на кол во строк
#mean(1) сложит столбы и поделит на кол во столбцов
#.shape() (2, 5)