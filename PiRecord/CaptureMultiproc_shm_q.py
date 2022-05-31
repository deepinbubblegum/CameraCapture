import time
import yaml
import subprocess as sp
import atexit
import numpy as np

class CaptureUDP():
    def __init__(self, width=1920, height=1080, fps=50):
        # self.width = width
        # self.height = height
        # self.fps = fps
        self.width, self.height, self.fps, self.ipaddress, self.prot = self.load_config()
        print(self.ipaddress, self.prot)
        
    def load_config(self):
        with open('config/piconfig.yaml', 'r') as fileconfig:
            conf = yaml.safe_load(fileconfig)
        width = conf['target']['width']
        height = conf['target']['height']
        fps = conf['target']['fps']
        ip = conf['target']['ipaddress']
        port = conf['target']['prot']
        return width, height, fps, ip, port

    def camera_subprocess(self, width, height, fps, ipaddress, prot):
        start_time = time.time()
        N_frames = 0
        MAX_frames = 50
        bytesPerFrame = int(width*height*3/2)

        videoCmd = f'libcamera-vid -n --framerate {fps} --width {width} --height {height} -t 0 --codec yuv420 -o -'
        print(videoCmd)
        videoCmd = videoCmd.split()
        cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=1)
        atexit.register(cameraProcess.terminate)
        while True:
            yuv = np.frombuffer(cameraProcess.stdout.read(bytesPerFrame), dtype=np.uint8).reshape((height*3//2, width))
            if yuv.size != bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            # sender
            # pipe.send(yuv) # pipe
            
            cameraProcess.stdout.flush()
            N_frames += 1
            end_time = time.time()
            elapsed = end_time-start_time
            print("\033[2J\033[1;1H Result: "+str(N_frames/elapsed)+" fps")
            if N_frames > MAX_frames:
                N_frames = 0
                start_time = time.time()
    def start(self):
        