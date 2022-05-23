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

bool streamCapture::setParamsCapture(int capture_width, int capture_height, int framerate)
{
    string pi_pipe = gstreamer_pipeline(capture_width, capture_height, framerate);
    width = capture_width;
    height = capture_height;
    fps = framerate;
    video_cap = cap_pi(pi_pipe);
    return true;
}

string streamCapture::gstreamer_pipeline(int capture_width, int capture_height, int framerate) {
    return
        " libcamerasrc ! video/x-raw,format=YUY2,"
        " width=(int)" + std::to_string(capture_width) + ","
        " height=(int)" + std::to_string(capture_height) + ","
        " framerate=(fraction)" + std::to_string(framerate) +"/1 !"
        " decodebin ! videoconvert ! queue !"
        " appsink";
}

cv::VideoCapture streamCapture::cap_pi(string pi_pipe){
    cv::VideoCapture cap(pi_pipe, cv::CAP_GSTREAMER);
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
    cout << "campi init" << endl;
    if(!video_cap.isOpened())
    {
        exit(0);
    }

    cout << "Capture is opened." << endl;
    width = video_cap.get(3);
    height = video_cap.get(4);
    fps = video_cap.get(5);
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
        video_cap >> frame;
        frameSeq.push_back(frame);
        fps_now = cv::getTickFrequency() / (cv::getTickCount() - start);
        std::cout<< u8"\033[2J\033[1;1H"; // linux clear screen console
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
        // if (!this->isRunning_)
        //     break;
    }
    video_cap.release();
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
            outputVideo.open(genFile_name(), fourcc, fps, size);
            while (true)
            {
                if(!frameSeq.empty()){
                    outputVideo << frameSeq.front();
                    frameSeq.pop_front();
                    count_frame++;
                    cout << "frame :" << count_frame << endl;
                }
                if (count_frame >= (video_range * fps)){
                    count_frame = 0;
                    break;
                }
            }
            if (!this->isRunning_)
            {
                outputVideo.release();
                break;
            }
        }
    }
}