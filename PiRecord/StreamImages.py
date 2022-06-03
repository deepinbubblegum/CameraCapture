from threading import Thread
import time
import cv2
import subprocess as sp 
import glob
import os
import yaml

# rtsp://192.168.2.41/live.stream

class StreamImages():
    def __init__(self):
        self.width, self.height, self.fps, self.ipaddress, self.port, self.dir_name, self.time = self.load_config()
        self.fps = self.fps / 2
        self.udp_server = 'udp://192.168.2.222:20001'
        
    def command(self):
        command = ['ffmpeg',
           '-re',
           '-f', 'rawvideo',  # Apply raw video as input - it's more efficient than encoding each frame to PNG
           '-s', f'{self.width}x{self.height}',
           '-pixel_format', 'bgr24',
           '-r', f'{self.fps}',
           '-i', '-',
           '-f', 'mpegts',
           '-muxdelay', '0.1',
           self.udp_server
        ]
        return command

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

    def update(self):
        process = sp.Popen(self.command(), stdin=sp.PIPE)  # Execute FFmpeg sub-process for RTSP streaming
        N_image = 0
        sleeptime = 1/self.fps
        time.sleep(10)
        while True:
            try:
                current_img = cv2.imread(f'{self.dir_name}/image'+ str(N_image).zfill(10) + '.jpg')
            except:
                continue
            N_image += 2
            process.stdin.write(current_img.tobytes())
            time.sleep(sleeptime)

        process.stdin.close()  # Close stdin pipe
        process.wait()  # Wait for FFmpeg sub-process to finish
        ffplay_process.kill()  # Forcefully close FFplay sub-process
        print('end task stream')

    def start(self):
        thr = Thread(target=self.update, args=())
        thr.daemon = True
        thr.start()