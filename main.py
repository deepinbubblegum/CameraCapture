#!/usr/bin/python3
from PiRecord import CaptureMode, FileServer, StreamImages

def main():
    serv_ = FileServer()
    serv_.start()
    cap_ = CaptureMode()
    cap_.start()
    # stmi_ = StreamImages()
    # stmi_.start()


if __name__ == '__main__':
    main()