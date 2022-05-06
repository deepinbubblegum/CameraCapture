#include <iostream>
#include <detectGPU.hpp>

int main(void) {
    detectGPU objCal; //สร้าง Object ของ Class cal
    std::cout << "Hello, world!" << std::endl;
    std::cout << "Call class" << objCal.plus(1,2) << std::endl;
    return (0);
}
