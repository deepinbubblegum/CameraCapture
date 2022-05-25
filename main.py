from PiRecord import Capture
import time

width=1920
height=1080
fps=50
video_range = 10 #sec

cap_ = Capture(width, height, fps)
cap_.start()
N_frames = 0
MAX_frames = fps * video_range
start_time = time.time()

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