#!/usr/bin/python3
from time import sleep
from PiRecord import CaptureMode, FileServer, StreamImages

def main():
    serv_ = FileServer()
    serv_.start()
    cap_ = CaptureMode()
    cap_.start()
    sleep(20)
    cap_.stop()

if __name__ == '__main__':
    main()