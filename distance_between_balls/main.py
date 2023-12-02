import socket
import matplotlib.pyplot as plt
import numpy as np

def recall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

host = "84.237.21.36"
port = 5151

plt.ion()
plt.figure()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    
    beat = b"nope"
    while beat != b"yep":
        sock.send(b"get")
        bts = recall(sock, 80004)
        print(len(bts))

        im1 = np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0], bts[1])
        im2 = np.frombuffer(bts[40004:], dtype="uint8").reshape(bts[40002], bts[40003])

        pos1 = np.unravel_index(np.argmax(im1), im1.shape)
        pos2 = np.unravel_index(np.argmax(im2), im2.shape)
        res = np.abs(np.array(pos1)  - np.array(pos2))

        sock.send(f"{res[0]} {res[1]}".encode())
        print(sock.recv(4))

        plt.clf()
        plt.subplot(121)
        plt.title(str(pos1))
        plt.imshow(im1)
        plt.subplot(122)
        plt.title(str(pos2))
        plt.imshow(im2)
        plt.pause(10)

        sock.send(b"beat")
        beat = sock.recv(20)
    