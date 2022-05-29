import yaml

class CaptureUDP():
    def __init__(self, width=1920, height=1080, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.ipaddress, self.prot = self.load_config()
        print(self.ipaddress, self.prot)
        
    def load_config(self):
        with open('config/config.yaml', 'r') as fileconfig:
            conf = yaml.safe_load(fileconfig)
        return conf['target']['ipaddress'], conf['target']['prot']

    def camera_subprocess(self):
        pass
