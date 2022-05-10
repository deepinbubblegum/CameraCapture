#include <iostream>
#include <detectGPU.hpp>
#include <streamCapture.hpp>
#include <thread>

using namespace std;

void startCapture(streamCapture stream){
    stream.capture();
}

int main() {
    detectGPU detect_gpu;
    detect_gpu.checkDeviceInfo();
    streamCapture stream;
    string rtsp_uri = "rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=0 ! decodebin ! videoconvert ! queue ! appsink sync=true";
    stream.setStart(rtsp_uri, 10);
    thread setCapthread(startCapture, stream);
    setCapthread.join();
    // cout << "RTSP Capture Start!\n";
    // system("pause"); //windows Press any key to continue . . .
    // system("read"); // Linux and Mac 

    // #ifdef _WIN32
    
    // #endif
    return 0;
}
