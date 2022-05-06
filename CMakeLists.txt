cmake_minimum_required(VERSION 3.0.0)
project(RTSP_Capture VERSION 0.1.0)

include(CTest)
enable_testing()

add_subdirectory(RTSPCapture)
add_subdirectory(detectGPU)
# add_subdirectory(streamCapture)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)