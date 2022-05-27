from time import sleep
from PiRecord import Capture
from threading import Thread

width=1920
height=1080
fps=50
cap_ = Capture(width, height, fps)
cap_.start()
while True:
    if cap_.ret():
        yuv420 = cap_.read()
        sleep(0.02)
    else:
        sleep(1)