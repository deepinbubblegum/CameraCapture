#!/usr/bin/python3
from PiRecord import CaptureMode, FileServer

def main():
    cap_ = CaptureMode()
    cap_.start()
    serv_ = FileServer()
    serv_.start()

if __name__ == '__main__':
    main()