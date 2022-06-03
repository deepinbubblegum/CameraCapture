#!/usr/bin/python3
from time import sleep
from PiRecord import CaptureMode, FileServer, StreamImages
import socket


def send(msg, addr):
    msg = bytes(msg, 'utf-8')
    sock.sendto(msg, addr)

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
                send(f'set start', addr)
            elif set[1] == 'start' and isSetDir is False:
                print('Pless set dir name.')
                send(f'Pless set dir name.', addr)
            elif set[1] == 'stop' and isStart is True:
                cap_.stop()
                isStart = False
                isSetDir = False
            elif set[1] == 'stop' and isStart is False:
                print('Process not start.')
                send(f'Process not start.', addr)
            else:
                isSetDir = True
                cap_.setProject(set[1])
                dirname = set[1]
                send(f'set dir name "{dirname}"', addr)
        # elif set[0] == '!rm' and len(set) == 2 and isStart == False and set[1] != '/':
        #     dirname = set[1]
        #     send(f'remove dir name "{dirname}"', addr)
        #     recve_log = cap_.removeDir(dirname)
        #     send(f'{recve_log}', addr)
        # elif set[0] == '!rm' and len(set) == 2 and isStart == True:
        #     send(f'capture process is running can`t remove dir "{dirname}"', addr)
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