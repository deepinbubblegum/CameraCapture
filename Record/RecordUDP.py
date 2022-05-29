from ntpath import join
import struct
import subprocess
import yaml
import socket
import numpy as np
from threading import Thread
import cv2

class RecordUDP():
    def __init__(self):
       self.ports = self.load_config()
       self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       self.width = 1920
       self.height = 1080
       self.bytesPerFrame = self.width*self.height*3//2

    def load_config(self):
        with open('config/record.yaml', 'r') as ports_file:
            ports = yaml.safe_load(ports_file)['ports']
        return ports

    def recive_cam(self, sock, port):
        sock.bind(('0.0.0.0', port))
        dat = b''
        while True:
            seg, addr = sock.recvfrom(2**16)
            img = np.fromstring(seg, dtype=np.uint8)
            print(img)
            # exit()
            # yuv = np.fromstring(seg, dtype=np.uint8)
            # yuv = yuv.reshape((self.height*3//2, self.width))
            # print(yuv)
            # yuv = yuv.reshape((self.height*3//2, self.width))
            cv2.imshow('previwe', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    def start(self):
        threadings = []
        for port in self.ports:
            threadings.append(Thread(target=self.recive_cam, args=(self.sock, port,)))

        for thr in threadings:
            thr.daemon = True
            thr.start()

        for thr in threadings:
            thr.join()