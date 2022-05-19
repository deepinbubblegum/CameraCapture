from time import sleep
import cv2
from threading import Thread
from PiRecord import Capture
class Record():
    def __init__(self):
        self.capture = Capture()
        self.isRunning = False
        self.fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        self.out = cv2.VideoWriter('output.avi', self.fourcc, 30, (1280, 720))
        cv2.setUseOptimized(True)

    def writefile(self):
        while self.isRunning:
            if self.capture.ret() is True:
                frame = self.capture.read()
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_YUV420p2RGB)
                self.out.write(frame_rgb)

    def stop(self):
        self.isRunning = False

    def start(self):
        self.capture.start()
        self.isRunning = True
        thr = Thread(target=self.writefile, args=())
        thr.daemon = True
        thr.start()
        return self