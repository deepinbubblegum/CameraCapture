import yaml
import subprocess as sp

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
        videoCmd = f'libcamera-vid -n --framerate {fps} --width {width} --height {height} -t 0 --codec yuv420 --inline -o udp://{ipaddress}:{prot}'
        print(videoCmd)
        videoCmd = videoCmd.split()
        sp.run(videoCmd)

    def start(self):
        self.camera_subprocess(self.width, self.height, self.fps, self.ipaddress, self.prot)