cmake_minimum_required(VERSION 3.0.0)
project(detectGPU)

find_package( OpenCV REQUIRED )
add_library(detectGPU STATIC src/detectGPU.cpp)
include_directories(${OpenCV_INCLUDE_DIRS})
target_include_directories(detectGPU PUBLIC include)
target_link_libraries(detectGPU ${OpenCV_LIBS})