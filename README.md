gstreamer-1.0-msvc-x86_64-1.20.1
gstreamer-1.0-devel-msvc-x86_64-1.20.1

rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=100 ! decodebin ! videoconvert ! queue ! appsink sync=true