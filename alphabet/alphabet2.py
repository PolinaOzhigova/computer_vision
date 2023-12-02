import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from scipy.ndimage import binary_closing

struct = [[1, 1], [1, 1]]

def filling_factor(region):
    return region.image.mean()


def recognize(region):

    if filling_factor(region) == 1:
        return "-"

    euler = region.euler_number

    match euler:
        case -1:  # B or 8
            if 1 in region.image.mean(0):
                if region.image[0][0] == 0 and region.image[1][1] == 0:
                    return "8"
                return "B"
            return "8"
        case 0:  # A or 0 or D or P
            if 1 in region.image.mean(0): #D or P
                # print(region.filled_area - region.area)
                # plt.imshow(region.image)
                # plt.show()
                if region.filled_area - region.area < 100:
                    if region.image[0][0] == 0 and region.image[1][1] == 0:
                        return "0"
                    return "P"
                else:
                    return "b"
            tmp = region.image.copy()
            tmp[-1, :] = 1
            tmp_regions = regionprops(label(tmp))
            if tmp_regions[0].euler_number == -1:
                # plt.imshow(region.image)
                # plt.show()
                return "A"
            return "0"
        case _:  # 1 W X / *
            if 1 in region.image.mean(0):
                c = region.image.shape[0] - 1
                if region.image[c][0] == 0 and region.image[c][1] == 0:
                    return "*"
                # plt.imshow(region.image)
                # plt.show()
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

img = plt.imread('symbols.png')
# plt.imshow(img)
# plt.show()

binary = img.mean(2)
binary[binary>0] = 1
binary = binary_closing(binary, struct)
labeled = label(binary)
print(labeled.max(), " символов всего")

regions = regionprops(labeled)

counts = {}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1
print(len(counts), " из 12 (количество найденных типов символов)")
print(counts)
print(round(1.0 - counts.get("?", 0)/labeled.max(), 4)*100, "%")