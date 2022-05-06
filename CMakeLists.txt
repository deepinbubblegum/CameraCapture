cmake_minimum_required(VERSION 3.0.0)
project(RTSP_Capture VERSION 0.1.0)

include(CTest)
enable_testing()

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(RTSP_Capture main.cpp)

target_link_libraries(RTSP_Capture ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
