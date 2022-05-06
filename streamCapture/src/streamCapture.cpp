#include <streamCapture.hpp>

void CaptureRTSP(string rtsp_url){
    if (rtsp_url == ""){
        cout << "error rtsp url" << endl;
        exit(0);
    }
    VideoCapture capture(rtsp_url, CAP_FFMPEG);
    if (!capture.isOpened()){
        cout << "Cannot open RTSP stream" << endl;
    }
    capture.release();
}