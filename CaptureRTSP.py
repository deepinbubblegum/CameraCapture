import os
import cv2
from threading import Thread
from queue import Queue
import time

class CaptureRTSP:
    def __init__(self, uri, username=None, password=None, queueSize=256):
        self.cap = self.ConnectUri(uri)
        f_width = int(self.cap.get(3))
        f_height = int(self.cap.get(4))
        f_fps = int(self.cap.get(5))
        # thread stop flag
        self.stopped = False
        if f_fps == 0:
            self.stopped = True
        # create queue frame
        self.queue_frame = Queue(maxsize=queueSize)
        # show frame size
        print(f_width, f_height, f_fps, queueSize)

    def ConnectUri(self, uri):
        rtsp_gst = f'rtspsrc location={uri} ! autovideosink'
        print(rtsp_gst)
        cap = cv2.VideoCapture(
            rtsp_gst, 
            cv2.CAP_GSTREAMER
        )
        # cap = cv2.VideoCapture(uri)
        return cap

    def CaptureFrame(self):
        while self.cap.isOpened():
            if self.stopped:
                return
            ret, frame = self.cap.read()
            if ret is False:
                self.stop()
            self.queue_frame.put(frame)

    def read(self):
        return self.queue_frame.get()

    def ret(self):
        return self.queue_frame.qsize() > 0

    def stop(self):
        self.stopped = True

    def start(self):
        # start a thread to read frames from the file video stream
        t = Thread(target=self.CaptureFrame, args=())
        t.daemon = True
        t.start()
        return self