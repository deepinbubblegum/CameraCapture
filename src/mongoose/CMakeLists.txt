cmake_minimum_required(VERSION 3.0.0)
project(mongoose)

add_library(mongoose SHARED mongoose.c)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
find_package (Threads)
target_link_libraries (mongoose ${CMAKE_THREAD_LIBS_INIT} ${CMAKE_DL_LIBS})

install(TARGETS mongoose DESTINATION lib)
install(FILES mongoose.h DESTINATION include)

if(WIN32)
    find_library(WSOCK32_LIBRARY wsock32)
    find_library(WS2_32_LIBRARY ws2_32)
    target_link_libraries(mongoose ws2_32 wsock32)
endif()