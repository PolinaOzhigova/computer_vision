import cv2
import zmq
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://192.168.0.100:6556")
cv2.namedWindow("Camera")

c = -1
while True:
    buffer = socket.recv()
    c += 1
    arr = np.frombuffer(buffer, np.uint8)
    frame = cv2.imdecode(arr, -1)
    cv2.putText(frame, f"{c}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(500)
    if key == ord("q"):
        break