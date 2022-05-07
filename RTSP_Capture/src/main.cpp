#include <iostream>
#include <detectGPU.hpp>
#include <streamCapture.hpp>

using namespace std;
int main() {
    detectGPU detect_gpu;
    detect_gpu.checkDeviceInfo();
    streamCapture stream;
    stream.run();
    cout << "RTSP Capture stop!\n";
    system("pause"); //windows
    // system("read"); // Linux and Mac 
    return 0;
}
