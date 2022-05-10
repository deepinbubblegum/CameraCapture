#include <streamCapture.hpp>

string streamCapture::genFile_name(){
    time_t t = time(0);
    struct tm* now = localtime(&t);
    char buffer[80];
    strftime(buffer, 80, "%F_%H-%M-%S", now);
    string a_name = (string)buffer + "." + file_type;
    return a_name;
}

void streamCapture::capture(){
    cv::VideoCapture cap(rtsp_uri, cv::CAP_GSTREAMER);
    if (!cap.isOpened()){
        exit(0);
    }
    cout << "Capture is opened." << endl;
    width = cap.get(3);
    height = cap.get(4);
    fps = cap.get(5);
    if (width == 0 && height==0){
        cout << "Capture can't capture frame." << endl;
        exit(0);
    }
    cout << "Width : " << width << ", ";
    cout << "Height: " << height << ", ";
    cout << "fps: " << fps << endl;
    size = cv::Size((int)width, (int)height);
    int count_frame = 0;
    string file_name = "videos";
    createDirectory(file_name);;
    while(true){
        file_name = "videos/" + (string)genFile_name();
        outputVideo.open(file_name, fourcc, fps, size);
        while(true){
            cap >> frame;
            frameSeq.push_back(frame);
            outputVideo << frameSeq.front();
            count_frame++;
            if (count_frame >= (video_range * fps)) break;
        }
        count_frame = 0;
        if (stop){
            outputVideo.release();
            break;
        }
    }
    cap.release();
}

bool streamCapture::setStart(string url, double video_sec){
    video_range = video_sec;
    rtsp_uri = url;
    return true;
}

bool streamCapture::setStop(){
    stop = true;
    return true;
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