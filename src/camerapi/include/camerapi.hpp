#include <iostream>
#include <vector>
#include <string>
#include <fcntl.h>
#include <array>
#include <opencv2/opencv.hpp>
using namespace std;
class CameraPi
{
private:
    int width, width2, height, height2;
    int FPS;
    int nb; //bytes per frame
    vector<char> bufferSeq;
    size_t count;
    FILE *pipe;

    // cv::Mat Y;

    string cmdSetCamera();
public:
    bool init(int width, int height, int fps);
    bool readFrame();
};