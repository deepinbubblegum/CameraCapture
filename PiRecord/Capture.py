import cv2
import numpy as np
import libcamera
from picamera2 import Picamera2
from queue import Queue
from threading import Thread
import time


class Capture():
    def __init__(self):
        print("init record")
        self.picam2 = Picamera2()
        FrameDurationMain = (int)((1/29.97) * pow(10, 6))
        FrameDurationLores = (int)((1/29.97)* pow(10, 6))
        print(FrameDurationMain, FrameDurationLores)
        config = self.picam2.video_configuration(
            main={
                "size": (1280, 720),
                "format": "BGR888"
            },
            lores={
                "size": (1280, 720),
                "format": "YUV420"
            },
            controls = {
                "NoiseReductionMode": libcamera.NoiseReductionMode.Fast,  # Fast # Minimal # HighQuality
                "FrameDurationLimits": (FrameDurationMain, FrameDurationLores)
            },
            buffer_count=9,
        )
        self.picam2.configure(config)
        self.queue_frame = Queue()
        self.isRuning = False

    def update(self):
        while self.isRuning:
            e1 = cv2.getTickCount()
            # RGB = self.picam2.capture_array("main")
            # frame_rgb = cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)
            yuv420 = self.picam2.capture_array("lores")
            # frame_rgb = cv2.cvtColor(yuv420, cv2.COLOR_YUV420P2BGR)
            # self.queue_frame.put(frame_rgb)
            thr_p = Thread(target=self.queue_put, args=(yuv420, ))
            thr_p.daemon = True
            thr_p.start()
            e2 = cv2.getTickCount()
            time = (e2 - e1)/ cv2.getTickFrequency()
            print("\033[2J\033[1;1H")
            print(1/time)

    def queue_put(self, frame):
        
        self.queue_frame.put(frame)

    def read(self):
        return self.queue_frame.get()

    def ret(self):
        # print("\033[2J\033[1;1H")
        # print(self.queue_frame.qsize())
        return self.queue_frame.qsize() > 0

    def stop(self):
        self.isRuning = False

    def start(self):
        self.picam2.set_controls({"AwbEnable": 15, "AeEnable": 15})
        self.picam2.start()
        self.isRuning = True
        thr = Thread(target=self.update, args=())
        thr.daemon = True
        thr.start()
        return self