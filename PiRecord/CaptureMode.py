import os
from threading import Thread
import yaml
import subprocess as sp
import ffmpeg

class CaptureMode():
    def __init__(self):
        self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name = self.load_config()
        os.makedirs(self.dir_name, exist_ok=True)
        
    def load_config(self):
        with open('config/piconfig.yaml', 'r') as fileconfig:
            conf = yaml.safe_load(fileconfig)
        width = conf['target']['width']
        height = conf['target']['height']
        fps = conf['target']['fps']
        ip = conf['target']['ipaddress']
        port = conf['target']['port']
        dir_name = conf['path']['dir']
        return width, height, fps, ip, port, dir_name

    def camera_subprocess(self, width, height, fps, ipaddress, port, dir_name):
        videoCmd = f'libcamera-vid -t 0 --framerate {fps} --width {width} --height {height} --codec mjpeg --segment 1 -o {dir_name}/%010d.jpeg'
        print(videoCmd)
        videoCmd = videoCmd.split()
        sp.run(videoCmd)

    def start(self):
        thread_cap = Thread(target=self.camera_subprocess, args=(self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name))
        thread_cap.daemon = True
        thread_cap.start()
        # thread_cap.join()