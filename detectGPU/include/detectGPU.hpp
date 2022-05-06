#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/cudaarithm.hpp>

using namespace std;
using namespace cv;
using namespace cv::cuda;
class detectGPU
{
    private:
        bool hasDevices = false;
    public:
        bool checkDeviceInfo();
};