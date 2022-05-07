#include <iostream>
#include <thread>
#include <opencv2/opencv.hpp>

using namespace std;
class streamCapture
{
private:
    cv::Mat frame;
    string rtsp_uri = "rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=5 ! rtph264depay ! h264parse ! decodebin ! videoconvert ! appsink";
    int resize_factor = 3;
public:
    double width, height;
    double fps;
    int run();
};