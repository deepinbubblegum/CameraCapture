#include <extractVideo.hpp>

// 182618, 182749
bool extractVideo::find_time_in_video(){
    for(int i; i < source_dir.size(); i++){
        cout << source_dir[i] << endl;
    }
    return true;
}

bool extractVideo::toImage(vector<string> dir, float time_start, float time_end){
    source_dir = dir;
    time_start = (int)round(time_start);
    time_end = (int)round(time_end);
    if (!find_time_in_video()){
        return false;
    }
    return true;
}