#include <streamCapture.hpp>

int streamCapture::capframe(){
    //thread
    return 0;
}


int streamCapture::run(){
    cv::VideoCapture cap(rtsp_uri, cv::CAP_GSTREAMER);
    if(!cap.isOpened()) {
        std::cout << "Cannot open RTSP stream" << std::endl;
        return -1;
    }
    width = cap.get(3);
    height = cap.get(4);
    fps = cap.get(5);
    if (width == 0 && height==0)
        return -1;

    cout << "Width : " << width << ", ";
    cout << "Height: " << height << ", ";
    cout << "fps: " << fps << endl;

    int w = (int)(width / resize_factor);
    int h = (int)(height / resize_factor);

    cv::namedWindow("RTSP stream", cv::WINDOW_NORMAL);
    cv::resizeWindow("RTSP stream", w, h);
    while (true)
    {
        cap >> frame;
        cv::imshow("RTSP stream", frame);
        if (cv::waitKey(1) == 27) {
            break;
        }
    }
    cap.release();
    cv::destroyAllWindows();
    return 0;
}