cmake_minimum_required(VERSION 3.0.0)
project(capture)
add_library(capture SHARED src/capture.cpp)
target_include_directories(capture PUBLIC include)