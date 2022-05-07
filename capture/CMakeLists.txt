add_library(capture STATIC src/capture.cpp)
add_library(captureStatic SHARED src/capture.cpp)
set_target_properties(captureStatic PROPERTIES OUTPUT_NAME capture)
target_include_directories(capture PUBLIC include)