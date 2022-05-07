#include <iostream>
#include <streamCapture.hpp>

using namespace std;
int main() {
    capture cap;
    cap.say_hello();
    cout << "RTSP Capture!\n";
    return 0;
}
