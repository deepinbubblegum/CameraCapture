#!/usr/bin/python3
from time import sleep
from PiRecord import CaptureMode, FileServer, StreamImages

def main():
    serv_ = FileServer()
    cap_ = CaptureMode()




    # cap_.start()
    # serv_.start()
    # sleep(30)
    # cap_.stop()

if __name__ == '__main__':
    main()