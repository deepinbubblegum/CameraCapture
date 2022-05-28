from multiprocessing import shared_memory, Process, Lock, Pipe, Array
from multiprocessing import cpu_count, current_process
import numpy as np
import subprocess as sp
import atexit
import time

class CaptureMultiproc():
    def __init__(self, width=1920, height=1080, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.video_range = 5
        # creating a pipe
        # self.parent_conn, self.child_conn = Pipe()

        self.np_arr_shape = (height*3//2, width)
        self.mp_array = Array("I", int(np.prod(self.np_arr_shape)), lock=Lock())
        self.np_array = np.frombuffer(self.mp_array.get_obj(), dtype="I")#.reshape(self.np_arr_shape)
        self.shared_memory = (self.mp_array, self.np_array)

    def recv_camera(self, np_arr_shape, shared_memory, width, height, fps, video_range):
        start_time = time.time()
        MAX_frames = fps * video_range
        N_frames = 0
        bytesPerFrame = int(width*height*3/2)
        mp_array, np_array = shared_memory

        videoCmd = f'libcamera-vid -n --framerate {fps} --width {width} --height {height} -t 0 --codec yuv420 -o -'
        videoCmd = videoCmd.split()
        cameraProcess = sp.Popen(videoCmd, stdout=sp.PIPE, bufsize=1)
        atexit.register(cameraProcess.terminate)
        while True:
            yuv = np.frombuffer(cameraProcess.stdout.read(bytesPerFrame), dtype=np.uint8) #.reshape((height*3//2, width))
            if yuv.size != bytesPerFrame:
                print("Error: Camera stream closed unexpectedly")
                break
            # sender
            # pipe.send(yuv) # pipe
            mp_array.acquire()
            np_array[:] = yuv
            cameraProcess.stdout.flush()
            N_frames += 1
            end_time = time.time()
            elapsed = end_time-start_time
            print("\033[2J\033[1;1H Result: "+str(N_frames/elapsed)+" fps")
            if N_frames > MAX_frames:
                N_frames = 0
                start_time = time.time()
    
    def recver_frame(self, shared_memory):
        mp_array, np_array = shared_memory
        while True:
            # _ = np_array
            # print(np_array)
            while True:
                try:
                    mp_array.release()
                    break
                # it already unlocked, wait until its locked again which means a new frame is ready
                except ValueError:
                    time.sleep(0.001)

    def start(self):
        # creating new processes
        p1 = Process(target=self.recv_camera, args=(self.np_arr_shape, self.shared_memory, self.width, self.height, self.fps, self.video_range, ))
        p2 = Process(target=self.recver_frame, args=(self.shared_memory,))

        # running processes
        p1.start()
        p2.start()

        # wait until processes finish
        p1.join()
        p2.join()