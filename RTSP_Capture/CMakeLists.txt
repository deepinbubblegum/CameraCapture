################################################################################
### Selecting CMake minimum version

cmake_minimum_required(VERSION 3.0.0)

################################################################################
### Setting Global Parameters

set(PROJECT_NAME "RTSP Capture")
set(BINARY_NAME "RTSP_Capture")

set(APP_VERSION_STRING 0.1.0)
set(APP_BASE_PATH "${PROJECT_SOURCE_DIR}/src")

set(THREADS_PREFER_PTHREAD_FLAG ON)
FIND_PACKAGE(Threads REQUIRED)

project(${PROJECT_NAME})
################################################################################
### Check Dependencies

INCLUDE(CheckIncludeFile)

################################################################################
### Project definition

add_executable(${BINARY_NAME} src/main.cpp)

install(TARGETS ${BINARY_NAME} DESTINATION bin)