cmake_minimum_required(VERSION 3.0.0)
project(capture)

find_package(OpenCV REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(LIBCAMERA REQUIRED libcamera)

add_library(capture SHARED src/capture.cpp)
target_include_directories(capture PUBLIC include)
include_directories(${LIBCAMERA_INCLUDE_DIRS} ${OPENCV_INCLUDE_DIRS})
target_link_libraries(capture -llccv ${OpenCV_LIBS})