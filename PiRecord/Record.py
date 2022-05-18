from tracemalloc import start
import cv2
from numpy import empty
from picamera2 import Picamera2

class Record():
    def __init__(self):
        print("init record")
        picam2 = Picamera2()

    def start(self):
        pass