import os
from threading import Thread
import yaml
import subprocess as sp
import shutil

class CaptureMode():
    def __init__(self):
        self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name, self.time = self.load_config()
        self.segment = int(1/self.fps * pow(10, 2))
        try:
            shutil.rmtree(self.dir_name)
        except:
            pass
        os.makedirs(self.dir_name, exist_ok=True)
        
    def load_config(self):
        with open('config/piconfig.yaml', 'r') as fileconfig:
            conf = yaml.safe_load(fileconfig)
        width = conf['target']['width']
        height = conf['target']['height']
        fps = conf['target']['fps']
        ip = conf['target']['ipaddress']
        port = conf['target']['port']
        time = conf['target']['time']
        dir_name = conf['path']['dir']
        return width, height, fps, ip, port, dir_name, time

    def camera_subprocess(self, width, height, fps, ipaddress, port, dir_name, segment, time):
        videoCmd = f'libcamera-vid -t {time} --framerate {fps} --width {width} --height {height} --codec mjpeg --segment {segment} -o {dir_name}/image%010d.jpg'
        print(videoCmd)
        videoCmd = videoCmd.split()
        sp.run(videoCmd)

    def start(self):
        thread_cap = Thread(target=self.camera_subprocess, args=(self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name, self.segment, self.time))
        thread_cap.daemon = True
        thread_cap.start()
        # thread_cap.join()