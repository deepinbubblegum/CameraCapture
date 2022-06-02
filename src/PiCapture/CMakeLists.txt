cmake_minimum_required(VERSION 3.0.0)
project(PiCapture VERSION 0.1.0)
add_executable(PiCapture main.cpp)
set_target_properties(PiCapture PROPERTIES LINK_FLAGS "-Wl,-rpath,./lib/")