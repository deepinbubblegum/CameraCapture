#include <streamCapture.hpp>

string streamCapture::genFile_name()
{
    time_t t = time(0);
    struct tm *now = localtime(&t);
    char buffer[80];
    strftime(buffer, 80, "%F_%H-%M-%S", now);
    string a_name = VIDEO_DIR + "/" + NAME_DIR + "/" + (string)buffer + "." + file_type;
    path_file_video.push_back(a_name);
    return a_name;
}

string streamCapture::getDir_Video()
{
    time_t t = time(0);
    struct tm *now = localtime(&t);
    char buffer[80];
    strftime(buffer, 80, "%F", now);
    return (string)buffer;
}

bool streamCapture::setParamsCapture(string url, double video_sec)
{
    video_range = video_sec;
    rtsp_uri = url;
    video_cap = cap_RTSP();
    return true;
}

bool streamCapture::setParamsCapture(int capture_width, int capture_height, int framerate, int display_width, int display_height)
{
    string pi_pipe = gstreamer_pipeline(capture_width, capture_height, framerate, display_width, display_height);
    width = capture_width;
    height = capture_height;
    fps = framerate;
    video_cap = cap_pi(pi_pipe);
    return true;
}

bool streamCapture::setParamsCapture(int capture_width, int capture_height, int framerate)
{
    width = capture_width;
    height = capture_height;
    fps = framerate;
    return true;
}

string streamCapture::gstreamer_pipeline(int capture_width, int capture_height, int framerate, int display_width, int display_height) {
    return
            " libcamerasrc bitrate=5000000 ! video/x-raw,format=NV12,"
            " width=(int)" + std::to_string(capture_width) + ","
            " height=(int)" + std::to_string(capture_height) + ","
            " framerate=(fraction)" + std::to_string(framerate) +"/1 !"
            " v4l2convert !"
            " appsink";
}

cv::VideoCapture streamCapture::cap_RTSP()
{
    cv::VideoCapture cap(rtsp_uri, cv::CAP_GSTREAMER);
    if (!cap.isOpened())
    {
        cout << "error capture is can`t open" << endl;
        exit(0);
    }
    return cap;
}



cv::VideoCapture streamCapture::cap_pi(string pipe)
{
    cv::VideoCapture cap(pipe, cv::CAP_GSTREAMER);
    if (!cap.isOpened())
    {
        cout << "error capture is can`t open" << endl;
        exit(0);
    }
    return cap;
}

bool streamCapture::setStopCapture()
{
    this->isRunning_ = false;
    task_.join();
    task_record_.join();
    return true;
}

vector<string> streamCapture::getPathFileVideo()
{
    return this->path_file_video;
}

bool streamCapture::setStartCapture()
{
    this->task_ = std::thread(&streamCapture::capture, this);
    cout << "capture thread start.\n";
    startRecord();
    return true;
}

void streamCapture::capture()
{
    this->isRunning_ = true;
    NAME_DIR = getDir_Video();
    raspicam::RaspiCam_Cv Camera;
    cout << "campi init" << endl;
    if(!Camera.open())
    {
        exit(0);
    }

    cout << "Capture is opened." << endl;
    // width = video_cap.get(3);
    // height = video_cap.get(4);
    // fps = video_cap.get(5);
    if (width == 0 && height == 0)
    {
        cout << "Capture can't capture frame." << endl;
        exit(0);
    }
    cout << "Width : " << width << ", ";
    cout << "Height: " << height << ", ";
    cout << "fps: " << fps << endl;
    size = cv::Size((int)width, (int)height);
    int count_frame = 0;
    createDirectory(VIDEO_DIR);
    string dir_video_stame = VIDEO_DIR + "/" + NAME_DIR;
    createDirectory(dir_video_stame);
    while (true)
    {
        int64 start = cv::getTickCount();
        // outputVideo.open(genFile_name(), fourcc, fps, size);
        // video_cap >> frame;
        Camera.grab();
        Camera.retrieve (frame);
        frameSeq.push_back(frame);
        fps_now = cv::getTickFrequency() / (cv::getTickCount() - start);
        std::cout<< u8"\033[2J\033[1;1H"; // linux clear screen console
        // std::cout << "FPS : " << fps << std::endl;
        cout << "FPS Min : " << fps_min << "FPS Max : " << fps_max << "FPS Curent now : " << fps_now << "FPS Avg : " << fps_avg << endl;
        fps_sum += fps_now;
        fps_avg = fps_sum / count_fps;
        if(count_fps > 100){
            if(fps_avg > fps_max)
                fps_max = fps_avg;
            else if(fps_avg < fps_min)
                fps_min = fps_avg;
        }else{
            fps_min = fps_avg;
            fps_max = fps_avg;
        }
        count_fps++;
        // count_frame = 0;
        if (!this->isRunning_)
            break;
    }
    Camera.release();
}

bool streamCapture::startRecord(){
    this->task_record_ = std::thread(&streamCapture::record_frame, this);
    cout << "record thread start.\n";
    return true;
}

void streamCapture::record_frame(){
    int count_frame = 0;
    while (this->isRunning_)
    {
        if(!frameSeq.empty()){
            outputVideo.open(genFile_name(), fourcc, 50, size);
            while (true)
            {
                if(!frameSeq.empty()){
                    // outputVideo << frameSeq.front();
                    frameSeq.pop_front();
                    count_frame++;
                    // cout << "frame :" << count_frame << endl;
                }
                if (count_frame >= (video_range * fps))
                    break;
            }
            count_frame = 0;
            if (!this->isRunning_)
            {
                outputVideo.release();
                break;
            }
        }
    }
}


// bool streamCapture::start(string url, double video_sec){
//     video_range = video_sec;
//     rtsp_uri = url;
//     capture();
//     return true;
// }

// // test funtions
// int streamCapture::test(){
//     cv::VideoCapture cap(rtsp_uri, cv::CAP_GSTREAMER);
//     if(!cap.isOpened()) {
//         std::cout << "Cannot open RTSP stream" << std::endl;
//         return -1;
//     }
//     width = cap.get(3);
//     height = cap.get(4);
//     fps = cap.get(5);
//     if (width == 0 && height==0)
//         return -1;

//     cout << "Width : " << width << ", ";
//     cout << "Height: " << height << ", ";
//     cout << "fps: " << fps << endl;

//     int w = (int)(width / resize_factor);
//     int h = (int)(height / resize_factor);

//     cv::namedWindow("RTSP stream front", cv::WINDOW_NORMAL);
//     cv::resizeWindow("RTSP stream front", w, h);
//     cv::namedWindow("RTSP stream back", cv::WINDOW_NORMAL);
//     cv::resizeWindow("RTSP stream back", w, h);
//     while (true)
//     {
//         cap >> frame;
//         frameSeq.push_back(frame);
//         cv::imshow("RTSP stream front", frameSeq.front());
//         cv::imshow("RTSP stream back", frameSeq.back());
//         if (cv::waitKey(1) == 27) {
//             break;
//         }
//         if (cv::getWindowProperty("RTSP stream front", cv::WND_PROP_VISIBLE) < 1)
//             break;
//         if (cv::getWindowProperty("RTSP stream back", cv::WND_PROP_VISIBLE) < 1)
//             break;
//     }
//     cap.release();
//     cv::destroyAllWindows();
//     cout << "RTSP stream CLOSED" << endl;
//     return 0;
// }