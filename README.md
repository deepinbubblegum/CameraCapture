sudo apt update
sudo apt install nvidia-driver-470 libnvidia-encode-470 libnvidia-decode-470 libdrm-dev
sudo apt install nvidia-cuda-toolkit

python3 setup.py build_ext --inplace