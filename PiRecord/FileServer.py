import http.server
import os
import shutil
import socketserver
from threading import Thread
import yaml


def load_config():
    with open('config/piconfig.yaml', 'r') as fileconfig:
        conf = yaml.safe_load(fileconfig)
    width = conf['target']['width']
    height = conf['target']['height']
    fps = conf['target']['fps']
    ip = conf['target']['ipaddress']
    port = conf['target']['port']
    dir_name = conf['path']['dir']
    return dir_name

PORT = 8000
DIRECTORY = load_config()
os.makedirs(DIRECTORY, exist_ok=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
        
class FileServer():
    def __init__(self):
        os.makedirs(DIRECTORY, exist_ok=True)

    def setserver(self):
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

    def start(self):
        thr_server = Thread(target=self.setserver, args=())
        thr_server.daemon = True
        thr_server.start()
        # thr_server.join()