gstreamer-1.0-msvc-x86_64-1.20.1
gstreamer-1.0-devel-msvc-x86_64-1.20.1

rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=5 ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! fakesink


rtspsrc location=rtsp://admin:Camera123@192.168.100.2:554/rtpstream/config1 latency=5 ! rtph265depay ! h265parse ! nvv4l2decoder ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! fakesink