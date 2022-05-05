import os
import cv2
import numpy as np
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"]="rtsp_transport;udp;hw_decoders_any;vaapi,vdpau"
os.environ["OPENCV_FFMPEG_WRITER_OPTIONS"]="hw_encoders_any;cuda"
from threading import Thread
from queue import Queue
import time
print(cv2.getBuildInformation())
class CaptureRTSP:
    def __init__(self, uri, username=None, password=None, queueSize=1024):
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
        cap = cv2.VideoCapture(
            uri, 
            cv2.CAP_FFMPEG
        )
        return cap

    def CaptureFrame(self):
        while self.cap.isOpened():
            if self.stopped:
                return
            ret, frame = self.cap.read()
            # _, frame = cv2.imencode('.jpg', frame)
            if ret is False:
                self.stop()
            self.queue_frame.put(frame)

    def read(self):
        return self.queue_frame.get()

    def ret(self):
        print(self.queue_frame.qsize())
        return self.queue_frame.qsize() > 0
    
    def write(self, file_name='temp', frame=None, type='mjpeg'):
        if type == 'mjpeg':
            _, jpg = cv2.imencode('.jpg', frame)
            data_encode = np.array(jpg)
            image_jpeg = (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + data_encode.tobytes() + b'\r\n')
            # print(type(image_jpeg))
            with open(f'{file_name}.mjpeg', 'ab') as file:
                file.write(image_jpeg)

    def stop(self):
        self.stopped = True

    def start(self):
        # start a thread to read frames from the file video stream
        t = Thread(target=self.CaptureFrame, args=())
        t.daemon = False
        t.start()
        return self