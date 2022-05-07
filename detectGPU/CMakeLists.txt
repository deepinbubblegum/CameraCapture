cmake_minimum_required(VERSION 3.0.0)
project(detectGPU)

find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})

add_library(detectGPU STATIC src/detectGPU.cpp)
target_include_directories(detectGPU PUBLIC include)
# add_library(detectGPUStatic SHARED src/detectGPU.cpp)
# set_target_properties(detectGPUStatic PROPERTIES OUTPUT_NAME detectGPU)
target_link_libraries(detectGPU ${OpenCV_LIBS})