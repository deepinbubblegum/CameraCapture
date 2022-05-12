cmake_minimum_required(VERSION 3.0.0)
project(CameraCapture)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON) # microsoft fucking fix windows visual studio community build missing *.lib and stupid 
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")

add_subdirectory(src)

#Custom target for Only Building
add_custom_target(build ALL)

#Custom target for build and debug with GDB
add_custom_target(build_and_debug ALL DEPENDS ${TARGET_BINARY})

#Board IP
set(BOARD_IP 10.1.10.190)

#Port no
set(PORT_NO 5555)

add_custom_command(TARGET build_and_debug POST_BUILD
COMMAND scp ${CMAKE_CURRENT_BINARY_DIR}/${TARGET_BINARY} root@${BOARD_IP}:/home/CameraCapture
COMMAND ssh -f -L${PORT_NO}:localhost:${PORT_NO} root@${BOARD_IP} 'gdbserver :${PORT_NO} ./${TARGET_BINARY}')