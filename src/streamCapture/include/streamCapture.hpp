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
    vector<string> path_file_video;
    string VIDEO_DIR = "videos";
    string NAME_DIR = "";
    string rtsp_uri = "";
    int inx_cam;

    int resize_factor = 2;
    
    double width, height;
    double fps;
    double fps_now = 0.0, fps_min = 0.0, fps_max=0.0, fps_sum=0.0, fps_avg=0.0;
    int count_fps;

    cv::VideoCapture video_cap;
    
    string genFile_name();
    string getDir_Video();
    void capture();
    thread task_, task_record_;
    bool isRunning_;
    cv::VideoCapture cap_pi(string pi_pipe);

    string gstreamer_pipeline(int capture_width, int capture_height, int framerate);

    bool startRecord();
    void record_frame();
public:
    ~streamCapture() {
         this->setStopCapture();
    } 
    bool setParamsCapture(int capture_width, int capture_height, int framerate);
    // int test();
    bool setStopCapture();
    bool setStartCapture();
    vector<string> getPathFileVideo();
};