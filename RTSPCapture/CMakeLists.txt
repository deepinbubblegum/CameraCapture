cmake_minimum_required(VERSION 3.0.0)
project(RTSPCapture VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(RTSPCapture 
    src/main.cpp
)
target_link_libraries(RTSPCapture detectGPU)
# target_link_libraries(RTSPCapture streamCapture)



set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)