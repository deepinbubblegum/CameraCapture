#!/usr/bin/python3
from time import sleep
from PiRecord import CaptureMode, FileServer, StreamImages
import socket

def main():
    serv_ = FileServer()
    serv_.start()
    cap_ = CaptureMode()
    isSetDir = False
    isStart = False
    while True:
        recv, addr = sock.recvfrom(1024) # buffer size is 1024 
        set = recv.decode("utf-8").split()
        if set[0] == '!set' and len(set) == 2:
            if set[1] == 'start' and isSetDir is True:
                cap_.start()
                isStart = True
            elif set[1] == 'start' and isSetDir is False:
                print('Pless set project name.')
            elif set[1] == 'stop' and isStart is True:
                cap_.stop()
                isStart = False
            elif set[1] == 'stop' and isStart is False:
                print('Process not start.')
            else:
                isSetDir = True
                cap_.setProject(set[1])
        else:
            print(f'Command "{set}" is not correct.')

if __name__ == '__main__':
    UDP_PORT = 5005
    sock = socket.socket(
        socket.AF_INET, # Internet
        socket.SOCK_DGRAM
    ) # UDP
    sock.bind(('', UDP_PORT))
    main()