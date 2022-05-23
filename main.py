import cv2
import numpy as np
import subprocess as sp
import time
import atexit

frames = []
max_frames = 300

N_frames = 0

# Video capture parameters
(w,h) = (1920,1080)
bytesPerFrame = w*h
fps = 60
videoCmd = f'libcamera-vid -n --framerate {fps} --width {w} --height {h} -t 0 --codec yuv420 -o -'
print(videoCmd)
videoCmd = videoCmd.split()

#cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE) # start the camera
cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=1)
atexit.register(cameraProcess.terminate)
rawStream = cameraProcess.stdout.read(bytesPerFrame)

print("Recording...")

start_time = time.time()

while True:
    cameraProcess.stdout.flush()
    frame = np.frombuffer(cameraProcess.stdout.read(bytesPerFrame), dtype=np.uint8)
    if frame.size != bytesPerFrame:
        print("Error: Camera stream closed unexpectedly")
        break
    # print(frame.shape)q
    frame.shape = (h, w)
    frames.append(frame)
    N_frames += 1
    if N_frames > max_frames: break

end_time = time.time()
cameraProcess.terminate() # stop the camera
elapsed_seconds = end_time-start_time
print("Done! Result: "+str(N_frames/elapsed_seconds)+" fps")

print("Writing frames to disk...")
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("video.avi", fourcc, 60, (w,h))
for n in range(N_frames):
    frame_rgb = cv2.cvtColor(frames[n],cv2.COLOR_YUV420p2RGB)
    out.write(frame_rgb)
out.release()

print("Display frames with OpenCV...")
for frame in frames:
    cv2.imshow("video", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()