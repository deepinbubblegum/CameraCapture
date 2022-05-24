#include <camerapi.hpp>

string CameraPi::cmdSetCamera(){
    return
        "libcamera-vid -n --framerate " + to_string(FPS) + " "
        "--width " + to_string(width) + " "
        "--height " + to_string(height) + " "
        "-t 0 --codec yuv420 -o - ";
}

bool CameraPi::init(int w, int h, int fps){
    width = w;
    height = h;
    width2 = 64*(w/64);
    height2 = 32*(h/64);
    nb = width2*height2*3/2;
    FPS = fps;
    return true;
}

bool CameraPi::readFrame(){
    string cmd = cmdSetCamera();
    cv::Size actual_size(1920, 1080);
    cv::Size half_size(960, 540);
    cout << cmd << endl;
    char buf[nb];
    pipe = popen(cmd.c_str(), "r");
    int count = 0;
    while (fgets(buf, nb, pipe) != NULL)
    {   
        // cv::Mat imageWithData = cv::Mat(nb, 1, CV_8U, buf.data()).clone();
        // cv::Mat YUV(actual_size, CV_8UC1, buf.data());
        // cv::Mat YUV = cv::imdecode(buf, );
        // cv::imshow("view", YUV);
        
        // bufferSeq.push_back(*buf);
        // cout << bufferSeq.front();
        // bufferSeq.pop_front();
    }
    pclose(pipe);
    return true;
}