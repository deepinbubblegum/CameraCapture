#include <iostream>
// #include <detectGPU.hpp>
#include <streamCapture.hpp>
#include <thread>
#include <extractVideo.hpp>
#include <chrono>

using namespace std;
int main() {
    streamCapture stream;
    string rtsp_uri = "rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=0 ! decodebin ! videoconvert ! queue ! appsink sync=true";
    stream.setParamsCapture(rtsp_uri, 10);
    stream.setStartCapture();


    // example get dir file
    while(true){
        vector<string> file_list = stream.getPathFileVideo();
        cout << "#################" << endl;
        for(string str : file_list)
            cout << str << endl;
        this_thread::sleep_for(10000ms);
    }

    // cout << "RTSP Capture Start!\n";
    // system("pause"); //windows Press any key to continue . . .
    // system("read"); // Linux and Mac 

    // #ifdef _WIN32
    
    // #endif
    return 0;
}
