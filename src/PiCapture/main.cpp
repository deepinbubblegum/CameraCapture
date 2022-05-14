#include <iostream>
#include <streamCapture.hpp>
#include <thread>
#include <chrono>

using namespace std;
int main(){
    streamCapture stream;
    cout << "################# CameraCapture Pi version #################" << endl;
    int capture_width = 640; //1280 ;
    int capture_height = 480; //720 ;
    int framerate = 15 ;
    int display_width = 640; //1280 ;
    int display_height = 480; //720 ;
    stream.setParamsCapture(capture_width, capture_height, framerate, display_width, display_height);
    stream.setStartCapture();

    while(true){
        vector<string> file_list = stream.getPathFileVideo();
        cout << "#################" << endl;
        for(string str : file_list)
            cout << str << endl;
        this_thread::sleep_for(10000ms);
    }
    return 0;
}