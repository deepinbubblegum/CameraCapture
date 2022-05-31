from time import sleep
from PiRecord import Capture, CaptureMultiproc_shm_array, CaptureUDP, CaptureMultiproc_shm_q
from threading import Thread

# Multi Thread
cap_ = Capture()
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