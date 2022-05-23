cmake_minimum_required(VERSION 3.0.0)
project(camerapi)
add_library(camerapi SHARED src/camerapi.cpp)
target_include_directories(camerapi PUBLIC include)