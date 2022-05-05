import cv2
from CaptureRTSP import CaptureRTSP
import time

# gpu_frame = cv2.cuda_GpuMat()
# gpu_frame.upload(frame)

def main():
    userName = 'admin'
    passWord = 'Camera123'
    auth = f'{userName}:{passWord}@'
    cap_rtsp = CaptureRTSP(f'rtsp://{auth}192.168.100.2:554/rtpstream/config1')        
    cap_ = cap_rtsp.start()
    while cap_.stopped is not True:
        if cap_.ret() is False:
            continue
        frame = cap_.read()
        cap_.write('cap',frame)
        # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("output", 1280, 720)
        # cv2.imshow("output", frame)
        # key = cv2.waitKey(1)
        # if key == ord('q'):
        #     cap_.stop()
        #     break
    cap_.stop()

if __name__ == '__main__':
    main()
