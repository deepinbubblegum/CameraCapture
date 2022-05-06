#include <iostream>
#include <detectGPU.hpp>

using namespace std;
int main(void) {
    detectGPU detect_gpu;
    cout << " " << detect_gpu.checkDeviceInfo() << endl;
    // streamCapture.CaptureRTSP("rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1");
    return (0);
}
