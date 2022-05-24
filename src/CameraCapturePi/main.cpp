#include <iostream>
#include <camerapi.hpp>

int main(int, char**) {
    CameraPi camerapi;
    int width = 1920;
    int height = 1080;
    int fps = 60;

    camerapi.init(width, height, fps);
    camerapi.readFrame();
    return 0;
}