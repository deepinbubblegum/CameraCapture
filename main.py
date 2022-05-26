from PiRecord import Capture, Reacord
import time
width=1920
height=1080
video_range = 5 #sec
fps=50
cap_ = Capture(width, height, fps)
rec_ = Reacord(fps, video_range)
cap_.start()
start_time = time.time()
N_frames = 0
MAX_frames = fps * video_range
while True:
    if cap_.ret:
        # rec_.push(cap_.read())
        cap_.read()
        N_frames += 1
        end_time = time.time()
        elapsed = end_time-start_time
        print("\033[2J\033[1;1H Result: "+str(N_frames/elapsed)+" fps")
        if N_frames > MAX_frames:
            N_frames = 0
            start_time = time.time()
        # frame_rgb = cv2.cvtColor(yuv420, cv2.COLOR_YUV2BGR_I420)