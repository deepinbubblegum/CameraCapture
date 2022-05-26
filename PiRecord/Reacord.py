import numpy as np
from threading import Thread
import time
class Reacord():
    def __init__(self, fps=30, video_range=10):
        self.video_range = 10 #sec
        self.frame_list = []
        self.mxframe_list = fps * video_range

    def arr_save(self, frame_arr):
        np.save('/dev/shm/data.npy', frame_arr)
        self.frame_list.clear()

    def push(self, frame):
        self.frame_list.append(frame)
        if len(self.frame_list) == self.mxframe_list:
            self.save()

    def save(self):
        thread_save = Thread(target=self.arr_save, args=(self.frame_list, ))
        thread_save.daemon = True
        thread_save.start()