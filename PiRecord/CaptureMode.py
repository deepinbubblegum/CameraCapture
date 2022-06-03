import os
from threading import Thread
import yaml
import subprocess
import signal

class CaptureMode():
    def __init__(self):
        self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name, self.time = self.load_config()
        self.segment = int(1/self.fps * pow(10, 2))
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
        videoCmd = f'libcamera-vid -n -t {time} --framerate {fps} --width {width} --height {height} --codec mjpeg --segment 1000 -o {dir_name}/image%010d.mjpeg'
        print(videoCmd)
        videoCmd = videoCmd.split()
        # sp.run(videoCmd)
        self.pro = subprocess.Popen(videoCmd) 

    def start(self):
        thread_cap = Thread(target=self.camera_subprocess, args=(self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name, self.segment, self.time))
        thread_cap.daemon = True
        thread_cap.start()

    def stop(self):
        self.pro.kill()