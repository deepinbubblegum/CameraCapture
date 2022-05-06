#include <iostream>
#include <detectGPU.hpp>

#include <stdio.h>
// #include <opencv2/opencv.hpp>
// #include <opencv2/objdetect/objdetect.hpp>
// #include <opencv2/videoio/videoio.hpp>
// #include <opencv2/imgcodecs/imgcodecs.hpp>

using namespace cv;

int main(int argc, const char** argv) {
    detectGPU detect_gpu;
    detect_gpu.checkDeviceInfo();
    // cout << " " << detect_gpu.checkDeviceInfo() << endl;
    // streamCapture.CaptureRTSP("rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1");
    // const std::string RTSP_URL = "rtsp://admin:Camera123@192.168.100.2:554";
 
    // #if WIN32
    //     _putenv_s("OPENCV_FFMPEG_CAPTURE_OPTIONS", "rtsp_transport;udp");
    // #else
    //     setenv("OPENCV_FFMPEG_CAPTURE_OPTIONS", "rtsp_transport;udp", 1);
    // #endif
 
    // Mat frame;
    // VideoCapture cap(RTSP_URL, CAP_FFMPEG);
 
    // if (!cap.isOpened()) {
    //     std::cout << "Cannot open RTSP stream" << std::endl;
    //     return -1;
    // }
 
    // while (true) {
    //     cap >> frame;
    //     imshow("RTSP stream", frame);
 
    //     if (waitKey(1) == 27) {
    //         break;
    //     }
    // }
 
    // cap.release();
    // destroyAllWindows();
 
    return (0);
}
