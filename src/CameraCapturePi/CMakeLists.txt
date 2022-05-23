cmake_minimum_required(VERSION 3.0.0)
project(CameraCapturePi VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(CameraCapturePi main.cpp)
target_link_libraries(CameraCapturePi LINK_PUBLIC camerapi)

set_target_properties(CameraCapturePi PROPERTIES LINK_FLAGS "-Wl,-rpath,./lib/")
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
