sudo apt update
sudo apt install nvidia-driver-470 libnvidia-encode-470 libnvidia-decode-470 libdrm-dev
sudo apt install nvidia-cuda-toolkit

python3 setup.py build_ext --inplace

ffmpeg -i "rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1" -vcodec -c copy -y 