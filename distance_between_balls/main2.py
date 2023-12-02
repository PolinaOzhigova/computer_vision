import socket
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import binary_erosion
import numpy as np
import math

struct = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
struct1 = [[1, 1], [1, 1]]

def centroid(labeled, label = 1):
    pos = np.where(labeled==label)
    return pos[0].mean(), pos[1].mean()

def recall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

host = "84.237.21.36"
port = 5152

plt.ion()
plt.figure()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    
    beat = b"nope"
    while beat != b"yep":
        sock.send(b"get")
        bts = recall(sock, 40002)

        im1 = np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0], bts[1])
        
        im1[im1 > 0] = 1
        plt.imshow(im1)
        plt.pause(1)

        x = []
        y = []
        labeled = label(im1)
        
        for i in range(labeled.max()):
            region_indices = np.where(labeled == i)

            if labeled.max() == 1:
                if (
                    np.any(im1[region_indices[0] + 1, region_indices[1]]) and
                    not np.any(im1[region_indices[0], region_indices[1] - 1]) and
                    not np.any(im1[region_indices[0] - 1, region_indices[1] - 1]) and
                    np.any(im1[region_indices[0], region_indices[1] + 1])
                ):
                    y1, x1 = np.mean(region_indices[0]), np.mean(region_indices[1])
                    y.append(y1)
                    x.append(x1)
                    print(y, x)
                    
                #     x1, y1 = np.where(labeled == 1)
                #     help_list  = []
                #     help_list.append(np.where(np.any(labeled[x1+1, y1]) and \
                #         not np.any(labeled[x1, y1 - 1]) and not np.any(labeled[x1-1, y1 - 1]) and \
                #         np.any(labeled[x1, y1 + 1])))
                #     print(help_list)
                    # labeled1 = binary_erosion(labeled1, struct)
                    # if labeled1.max() == 1:
                    #     labeled1 = binary_erosion(labeled1, struct1)
            else:
                y1, x1 = centroid(labeled, i+1)
                y.append(y1)
                x.append(x1)

        res = round(math.sqrt(abs(x[0] - x[1])**2 + abs(y[0] - y[1])**2), 1)
        print(res)

        sock.send(f"{res}".encode())
        print(sock.recv(4))

        # plt.clf()
        # plt.title(str(res))
        # plt.imshow(labeled)
        # plt.pause(1)

        sock.send(b"beat")
        beat = sock.recv(20)