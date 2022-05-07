#include <streamCapture.hpp>

int streamCapture::run(){
    // #if WIN32
    //     _putenv_s("OPENCV_FFMPEG_CAPTURE_OPTIONS", "rtsp_transport;udp;hw_decoders_any;vaapi,vdpau");
    //     _putenv_s("OPENCV_FFMPEG_WRITER_OPTIONS", "hw_encoders_any;cuda");
    // #else
    //     setenv("OPENCV_FFMPEG_CAPTURE_OPTIONS", "rtsp_transport;udp;hw_decoders_any;vaapi,vdpau", 1);
    //     setenv("OPENCV_FFMPEG_WRITER_OPTIONS", "hw_encoders_any;cuda", 1);
    // #endif
    // cv::VideoCapture cap(rtsp_uri, cv::CAP_FFMPEG);
    cv::VideoCapture cap(rtsp_uri, cv::CAP_GSTREAMER);
    if(!cap.isOpened()) {
        std::cout << "Cannot open RTSP stream" << std::endl;
        return -1;
    }
    width = cap.get(3);
    height = cap.get(4);
    fps = cap.get(5);
    cout << "Width : " << width << endl;
    cout << "Height: " << height << endl;
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