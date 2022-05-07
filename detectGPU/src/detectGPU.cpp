#include <detectGPU.hpp>

bool detectGPU::checkDeviceInfo(){
    if (showDetect){
        printShortCudaDeviceInfo(getDevice());
        int cuda_devices_number = getCudaEnabledDeviceCount();
        cout << "CUDA Device(s) Number: "<< cuda_devices_number << endl;
        DeviceInfo _deviceInfo;
        bool _isd_evice_compatible = _deviceInfo.isCompatible();
        cout << "CUDA Device(s) Compatible: " << _isd_evice_compatible << endl;
        if (cuda_devices_number > 0 && _isd_evice_compatible)
            hasDevices = true;
        else
            hasDevices = false;
        showDetect = false;
    }
    return hasDevices;
}