#!/usr/bin/python3
from time import sleep
from PiRecord import Record

def main():
    rec = Record()
    rec.start()
    while True:
        sleep(0.5)

if __name__ == '__main__':
    main()