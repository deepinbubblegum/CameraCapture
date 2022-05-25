from PiRecord import Capture
import cv2
import time

cap_ = Capture(width=1920, height=1080, fps=50)
cap_.start()
N_frames = 0
MAX_frames = 50 * 10
start_time = time.time()
# cv2.cvtColor(cap_.read(), cv2.COLOR_YUV2BGR_I420)
while True:
    if cap_.ret:
        cap_.read()
        N_frames += 1
    end_time = time.time()
    elapsed = end_time-start_time
    print("\033[2J\033[1;1H Result: "+str(N_frames/elapsed)+" fps")
    if N_frames > MAX_frames:
        N_frames = 0
        start_time = time.time()