import datetime
import os
from threading import Thread
import time
import yaml
import cv2

class Record():
    def __init__(self):
        print('init Record')
        self.ports = self.load_config()
        self.video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

    def load_config(self):
        with open('config/ports.yaml', 'r') as ports:
            ports = yaml.safe_load(ports)
        ports = ports['ports']
        return ports

    def genfilename(self):
        datetime_object = datetime.datetime.now()
        name = datetime_object.strftime("%Y_%m_%H_%M_%S")
        return f'{name}.avi'

    def capture(self, port):
        while True:
            cap = cv2.VideoCapture(f'udp://127.0.0.1:{port}', cv2.CAP_FFMPEG)
            if cap.isOpened():
                break
            else:
                print(f'Capture not opened port : {port}')
                print(f'Capture tay again.. : {port}')
                time.sleep(0.1)
            
        # create dir
        dir_name = f'resource/video/{port}'
        os.makedirs(dir_name, exist_ok=True)
        # get detial video
        width, height = int(cap.get(3)), int(cap.get(4))
        file_shape = (width, height)
        fps = round(cap.get(cv2.CAP_PROP_FPS))
        print(f'record:{port} width :{width} height :{height} fps :{fps}')
        video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")
        video_range = 10
        FramePerFile = fps * video_range
        n_frame = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            video_writer = cv2.VideoWriter(f'{dir_name}/{self.genfilename()}', video_codec, fps, file_shape)
            while n_frame < FramePerFile:
                ret, frame = cap.read()
                if not ret:
                    # print('drop frame..')
                    continue
                n_frame += 1
                video_writer.write(frame)
            n_frame = 0
        cap.release()

    def start(self):
        thrs = []
        for port in self.ports:
            thrs.append(Thread(target=self.capture, args=(port,)))
        for thr in thrs:
            thr.daemon = True
            thr.start()
        for thr in thrs:
            thr.join()