#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/filesystem.hpp>
#include <deque>
#include <time.h>
#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <thread>

using namespace std;
using namespace cv::utils::fs;
class streamCapture
{
private:
    double video_range = 10; // sec
    cv::Mat frame;
    deque<cv::Mat> frameSeq;
    int fourcc = cv::VideoWriter::fourcc('X', 'V', 'I', 'D');
    string file_type = "avi";
    cv::VideoWriter outputVideo;
    cv::Size size;

    string NAME_DIR;

    string rtsp_uri = "";
    int resize_factor = 2;
    bool stop = false;
    double width, height;
    double fps;
    
    string genFile_name();

public:
    bool setStart(string url, double video_sec);
    // int test();
    bool setStop();
    void capture();
    // bool start(string url, double range_sec);
};