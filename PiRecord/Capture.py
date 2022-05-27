import numpy as np
import subprocess as sp
from threading import Thread
from queue import Queue
import atexit
import time
class Capture():
    def __init__(self, width=1920, height=1080, fps=50):
        self.queue_frame = Queue()
        self.isRuning = False
        self.width = width
        self.height = height
        self.fps = fps
        self.video_range = 5 #sec
        self.width2 = int(64*(self.width/64))
        self.height2 = int(32*(self.height/32))
        self.bytesPerFrame = int(self.width2*self.height2*3/2)
        print(f'width={self.width}, height={self.height}, fps="{self.fps}, bytesPerFrame={self.bytesPerFrame}')

    def update(self):
        videoCmd = f'libcamera-vid -n --framerate {self.fps} --width {self.width} --height {self.height} -t 0 --codec yuv420 -o -'
        videoCmd = videoCmd.split()
        cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=2)
        atexit.register(cameraProcess.terminate)
        start_time = time.time()
        MAX_frames = self.fps * self.video_range
        N_frames = 0
        while self.isRuning:
            yuv = np.frombuffer(cameraProcess.stdout.read(self.bytesPerFrame), dtype=np.uint8).reshape((self.height2*3//2, self.width2))
            if yuv.size != self.bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            self.queue_frame.put(yuv)
            cameraProcess.stdout.flush()
            N_frames += 1
            end_time = time.time()
            elapsed = end_time-start_time
            print("\033[2J\033[1;1H Result: "+str(N_frames/elapsed)+" fps")
            if N_frames > MAX_frames:
                N_frames = 0
                start_time = time.time()
            
    def read(self):
        return self.queue_frame.get()

    def ret(self):
        return self.queue_frame.qsize() > 0

    def start(self):
        self.isRuning = True
        thread_cap = Thread(target=self.update, args=())
        thread_cap.daemon = True
        thread_cap.start()

    def stop(self):
        self.isRuning = False