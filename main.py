from time import sleep
from PiRecord import Capture, CaptureMultiproc
from threading import Thread

width=1920
height=1080
fps=50

# Multi Thread
# cap_ = Capture(width, height, fps)
# cap_.start()
# while True:
#     if cap_.ret():
#         yuv420 = cap_.read()
#         sleep(0.01)
#     else:
#         sleep(1)

Multi proc shm
cap_ = CaptureMultiproc(width, height, fps)
cap_.start()