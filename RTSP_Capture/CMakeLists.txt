add_executable(RTSP_Capture src/main.cpp)
target_link_libraries(RTSP_Capture detectGPU)
# target_link_libraries(RTSP_Capture streamCapture)