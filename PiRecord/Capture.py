import os
import socket
import numpy as np
import subprocess as sp
from threading import Thread
# from queue import Queue
from collections import deque
import atexit
import time
import yaml
import cv2
class Capture():
    def __init__(self):
        width, height, fps, ip, port = self.load_config()
        # self.queue_frame = Queue()
        self.queue_frame = deque()
        self.isRuning = False
        self.width = width
        self.height = height
        self.fps = fps
        # dir
        # dir_name = f'resource/video'
        # os.makedirs(dir_name, exist_ok=True)
        # writer fourcc
        self.video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

        self.video_range = 1 #sec
        self.width2 = int(64*(self.width/64))
        self.height2 = int(32*(self.height/32))
        self.bytesPerFrame = int(self.width2*self.height2*3/2)
        self.reshape_frame = (self.height2*3//2, self.width2)
        print(f'width={self.width}, height={self.height}, fps="{self.fps}, bytesPerFrame={self.bytesPerFrame}')
        # create cmd
        self.videoCmd = f'libcamera-vid --mode 1332:990:10 --framerate {self.fps} --width {self.width} --height {self.height} -t 0 --codec yuv420 -o -'
        print(self.videoCmd)
        self.videoCmd = self.videoCmd.split()
        self.cameraProcess = sp.Popen(self.videoCmd, stdout=sp.PIPE, bufsize=1)
        atexit.register(self.cameraProcess.terminate)

    def load_config(self):
        with open('config/piconfig.yaml', 'r') as fileconfig:
            conf = yaml.safe_load(fileconfig)
        width = conf['target']['width']
        height = conf['target']['height']
        fps = conf['target']['fps']
        ip = conf['target']['ipaddress']
        port = conf['target']['port']
        return width, height, fps, ip, port

    def update(self):
        start_time = time.time()
        MAX_frames = self.fps
        N_frames = 0
        while self.isRuning:
            self.cameraProcess.stdout.flush()
            yuv = np.frombuffer(self.cameraProcess.stdout.read(self.bytesPerFrame), dtype=np.uint8).reshape(self.reshape_frame)
            if yuv.size != self.bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            # self.queue_frame.put_nowait(yuv)
            frame_rgb = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
            self.queue_frame.append(frame_rgb)
            N_frames += 1
            end_time = time.time()
            elapsed = end_time-start_time
            print("\033[2J\033[1;1H Result: "+str(N_frames//elapsed)+" fps")
            if N_frames > MAX_frames:
                N_frames = 0
                start_time = time.time()

    def record(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            if self.ret():
                frame_rgb = self.read()
            else:
                time.sleep(0.002)

    def read(self):
        # return self.queue_frame.get()
        return self.queue_frame.popleft()

    def ret(self):
        # print(self.queue_frame.qsize())
        return self.queue_frame

    def start(self):
        self.isRuning = True
        thread_cap = Thread(target=self.update, args=())
        thread_rec = Thread(target=self.record, args=())

        thread_cap.daemon = True
        thread_rec.daemon = False

        thread_cap.start()
        thread_rec.start()

        thread_cap.join()
        thread_rec.join()

    def stop(self):
        self.isRuning = False