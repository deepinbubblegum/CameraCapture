cmake_minimum_required(VERSION 3.0.0)
project(extractVideo)

find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})
add_library(extractVideo SHARED src/extractVideo.cpp)
target_include_directories(extractVideo PUBLIC include)
target_link_libraries(extractVideo ${OpenCV_LIBS})