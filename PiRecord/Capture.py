import cv2
import numpy as np
import subprocess as sp
from threading import Thread
from queue import Queue
import atexit

class Capture:
    def __init__(self, width=1920, height=1080, fps=50):
        print("__init Camera")
        self.queue_frame = Queue()
        self.isRuning = False
        self.width = width
        self.height = height
        self.fps = fps
        self.width2 = int(64*(self.width/64))
        self.height2 = int(32*(self.height/32))
        self.bytesPerFrame = int(self.width2*self.height2*3/2)

    def update(self):
        videoCmd = f'libcamera-vid -n --framerate {self.fps} --width {self.width} --height {self.height} -t 0 --codec yuv420 -o -'
        videoCmd = videoCmd.split()
        cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=1)
        atexit.register(cameraProcess.terminate)
        rawStream = cameraProcess.stdout.read(self.bytesPerFrame)
        while self.isRuning:
            e1 = cv2.getTickCount()
            cameraProcess.stdout.flush()
            yuv = np.frombuffer(cameraProcess.stdout.read(self.bytesPerFrame), dtype=np.uint8).reshape((self.height2*3//2, self.width2))
            if yuv.size != self.bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            self.queue_frame.put(yuv)
            e2 = cv2.getTickCount()
            time = (e2 - e1)/ cv2.getTickFrequency()
            print("\033[2J\033[1;1H")
            print(1/time)

    def start(self):
        self.isRuning = True

    def stop(self):
        self.isRuning = False