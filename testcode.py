import cv2
import numpy as np
import subprocess as sp
import time
import atexit


frames = []
max_frames = 300

N_frames = 0

# Video capture parameters
(w,h) = (1920, 1080)

w2 = int(64*(w/64))
h2 = int(32*(h/32))
bytesPerFrame = int(w2*h2*3/2)
print("w2", w2)
print("h2", h2)
print(bytesPerFrame)
fps = 50
# print("Y shape: ", w2*h2)
videoCmd = f'libcamera-vid -n --framerate {fps} --width {w} --height {h} -t 0 --codec yuv420 -o -'
print(videoCmd)
videoCmd = videoCmd.split()

cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=1)
atexit.register(cameraProcess.terminate)
rawStream = cameraProcess.stdout.read(bytesPerFrame)

print("Recording...")
start_time = time.time()
while True:
    cameraProcess.stdout.flush()
    yuv = np.frombuffer(cameraProcess.stdout.read(bytesPerFrame), dtype=np.uint8).reshape((h2*3//2, w2))
    if yuv.size != bytesPerFrame:
        print("Error: Camera stream closed unexpectedly")
        break
    # frame_rgb = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
    # cv2.imshow('yuv', frame_rgb)
    # cv2.waitKey(1)
    # print(yuv)
    frames.append(yuv)
    N_frames += 1
    if N_frames > max_frames: break

end_time = time.time()
cameraProcess.terminate() # stop the camera
elapsed_seconds = end_time-start_time
print("Done! Result: "+str(N_frames/elapsed_seconds)+" fps")

# print("Writing frames to disk...")
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
# out = cv2.VideoWriter("video.avi", fourcc, 50, (w,h))
# for n in range(N_frames):
#     frame_rgb = cv2.cvtColor(frames[n], cv2.COLOR_YUV2BGR_I420)
#     out.write(frame_rgb)
# out.release()

print("Display frames with OpenCV...")
for n in range(N_frames):
    frame_rgb = cv2.cvtColor(frames[n], cv2.COLOR_YUV2BGR_I420)
    cv2.imshow("video", frame_rgb)
    cv2.waitKey(1)

cv2.destroyAllWindows()