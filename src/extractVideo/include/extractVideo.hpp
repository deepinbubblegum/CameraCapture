#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/filesystem.hpp>
#include <string>

using namespace std;
class extractVideo
{
private:
    vector<string> source_dir;
    int time_start, time_end;
    bool find_time_in_video();

public:
    bool toImage(vector<string> dir, float frame_start, float frame_end);
};