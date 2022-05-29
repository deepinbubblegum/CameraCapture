1920*1080 

libcamera-vid -n --framerate 50 --width 1920 --height 1080 -t 0 --codec yuv420 --inline -o udp://192.168.2.39:9000

ffplay udp://127.0.0.1:20001 -vf "setpts=N/50" -fflags nobuffer -flags low_delay -framedrop