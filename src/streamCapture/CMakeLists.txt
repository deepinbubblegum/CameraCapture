cmake_minimum_required(VERSION 3.0.0)
project(streamCapture)

find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})
add_library(streamCapture STATIC src/streamCapture.cpp)
target_include_directories(streamCapture PUBLIC include)
target_link_libraries(streamCapture ${OpenCV_LIBS})