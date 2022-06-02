1920*1080 

libcamera-vid -n --framerate 50 --width 1920 --height 1080 -t 0 --codec yuv420 --inline -o udp://192.168.2.39:9000

ffplay udp://127.0.0.1:20001 -vf "setpts=N/50" -fflags nobuffer -flags low_delay -framedrop


# ffmpeg -re -i "%WMSAPP_HOME%/content/sample.mp4" -pix_fmt yuv420p -vsync 1 -threads 0 -vcodec libx264 -r 30 -g 60 -sc_threshold 0 -b:v 512k -bufsize 640k -maxrate 640k -preset veryfast -profile:v baseline -tune film -acodec aac -b:a 128k -ac 2 -ar 48000 -af "aresample=async=1:min_hard_comp=0.100000:first_pts=0" -bsf:v h264_mp4toannexb -f mpegts udp://127.0.0.1:10000?pkt_size=1316


libcamera-vid --framerate 50 --mode 1332:990:10 --width 1280 --height 720 -t 0 --codec mjpeg --inline -o - | ffmpeg -re -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 50 -i pipe:0 -strict experimental -f mpegts udp://192.168.2.222:10000?pkt_size=1316

libcamera-vid --framerate 50 --mode 1332:990:10 --width 1280 --height 720 -t 0 --codec yuv420 --inline -o - | ffmpeg -re -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -vsync 1 -threads 4 -r 50 -i pipe:0 -strict experimental -f mpegts udp://192.168.2.222:20001


libcamera-vid -t 5000 --framerate 50 --width 1920 --height 1080 --codec mjpeg --segment 1 -o tmp%010d.tmp

libcamera-still -t 5000 --width 1280 --height 720 -e png --segment 30 -o test%06d.png