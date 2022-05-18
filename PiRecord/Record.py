import cv2
from threading import Thread
from PiRecord import Capture
class Record():
    def __init__(self):
        self.capture = Capture()
        self.isRunning = False
        self.fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        self.out = cv2.VideoWriter('output.avi', self.fourcc, 50.0, (1280, 720))

    def writefile(self):
        while self.isRunning:
            if self.capture.ret() is True:
                frame = self.capture.read()
                self.out.write(frame)

    def stop(self):
        self.isRunning = False

    def start(self):
        self.capture.start()
        self.isRunning = True
        thr = Thread(target=self.writefile, args=())
        thr.daemon = True
        thr.start()
        return self