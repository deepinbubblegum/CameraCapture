#include <iostream>
using namespace std;

// #include <opencv2/core.hpp>
#include<opencv2/opencv.hpp>
using namespace cv;

#include <opencv2/cudaarithm.hpp>
using namespace cv::cuda;
class streamCapture
{
private:

public:
    void CaptureRTSP(string uri);
};
