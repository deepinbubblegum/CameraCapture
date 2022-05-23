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
    cout << cmd << endl;
    char buffer[nb];
    pipe = popen(cmd.c_str(), "r");
    while (fgets(buffer, nb, pipe) != NULL)
    {   
        cout << buffer;
    }
    pclose(pipe);
    return true;
}