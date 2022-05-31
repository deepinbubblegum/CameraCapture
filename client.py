from time import sleep
from PiRecord import Capture, CaptureMultiproc_shm_array, CaptureUDP, CaptureMultiproc_shm_q
from threading import Thread

width=1920
height=1080
fps=30

# Multi Thread
cap_ = Capture(width, height, fps)
cap_.start()


# Multi proc shm
# cap_ = CaptureMultiproc_shm_array(width, height, fps)
# cap_.start()

# capture udp
# cap_ = CaptureUDP()
# cap_.start()

# Multi proc q
# cap_ = CaptureMultiproc_shm_q(width, height, fps)
# cap_.start()