cmake_minimum_required(VERSION 3.0.0)
project(detectGPU VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_library(detectGPU STATIC src/detectGPU.cpp)
target_include_directories(detectGPU PUBLIC include)

target_link_libraries(detectGPU ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)