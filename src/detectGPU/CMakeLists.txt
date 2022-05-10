cmake_minimum_required(VERSION 3.0.0)
project(detectGPU)

find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})
add_library(detectGPU SHARED src/detectGPU.cpp)
target_include_directories(detectGPU PUBLIC include)
target_link_libraries(detectGPU ${OpenCV_LIBS})