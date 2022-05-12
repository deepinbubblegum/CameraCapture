cmake_minimum_required(VERSION 3.0.0)
project(CameraCapture VERSION 0.1.0)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON) # microsoft fucking fix windows visual studio community build missing *.lib and stupid 
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")

add_subdirectory(src)