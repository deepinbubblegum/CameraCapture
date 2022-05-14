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
    video_cap = cap_pi(pi_pipe);
    return true;
}

string streamCapture::gstreamer_pipeline(int capture_width, int capture_height, int framerate, int display_width, int display_height) {
    return
            " v4l2src device=/dev/video0 ! video/x-raw, "
            " width=(int)" + std::to_string(capture_width) + ","
            " height=(int)" + std::to_string(capture_height) + ","
            " framerate=(fraction)" + std::to_string(framerate) +"/1 !"
            " videoconvert ! videoscale !"
            " video/x-raw,"
            " width=(int)" + std::to_string(display_width) + ","
            " height=(int)" + std::to_string(display_height) + " ! appsink";
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
    return true;
}

void streamCapture::capture()
{
    this->isRunning_ = true;
    NAME_DIR = getDir_Video();

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
        outputVideo.open(genFile_name(), fourcc, fps, size);
        while (true)
        {
            video_cap >> frame;
            frameSeq.push_back(frame);
            outputVideo << frameSeq.front();
            count_frame++;
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
    video_cap.release();
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