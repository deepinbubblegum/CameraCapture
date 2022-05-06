#include <iostream>
#include <detectGPU.hpp>

int main(void) {
    detectGPU detect_gpu;
    std::cout << "" << detect_gpu.checkDeviceInfo() << std::endl;
    return (0);
}
