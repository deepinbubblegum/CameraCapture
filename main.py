#!/usr/bin/python3
from PiRecord import Record

class CameraCapture():
    def __init__(self):
        record = Record()

    def start(self):
        pass

def main():
    cam_cap = CameraCapture()
    cam_cap.start()

if __name__ == '__main__':
    main()