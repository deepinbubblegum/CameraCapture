#include <iostream>
#include <vector>
#include <string>
#include <fcntl.h>
#include <array>
using namespace std;
class CameraPi
{
private:
    int width, width2, height, height2;
    int FPS;
    int nb; //bytes per frame
    
    size_t count;
    FILE *pipe;

    string cmdSetCamera();
public:
    bool init(int width, int height, int fps);
    bool readFrame();
};