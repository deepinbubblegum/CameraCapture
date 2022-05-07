#include <iostream>
#include <detectGPU.hpp>
// #include <streamCapture.hpp>

using namespace std;
int main() {
    detectGPU detect_gpu;
    detect_gpu.checkDeviceInfo();
    cout << "RTSP Capture!\n";
    return 0;
}
