#include <iostream>
#include <thread>
#include <opencv2/opencv.hpp>

using namespace std;
class streamCapture
{
private:
    cv::Mat frame;
    string rtsp_uri = "rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=0 ! decodebin ! videoconvert ! queue ! appsink sync=true";
    int resize_factor = 2.5;
    bool stop = false;

public:
    double width, height;
    double fps;
    int run();
};