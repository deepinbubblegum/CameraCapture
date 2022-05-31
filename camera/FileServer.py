import http.server
import os
import socketserver
from threading import Thread

PORT = 8000
DIRECTORY = "resource"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
        
class FileServer():
    def __init__(self) -> None:

        os.makedirs(DIRECTORY, exist_ok=True)

    def setserver(self):
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

    def start(self):
        thr_server = Thread(target=self.setserver, args=())
        thr_server.daemon = True
        thr_server.start()
        thr_server.join()
