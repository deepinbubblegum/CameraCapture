# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/CameraCapture

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/CameraCapture/build/Debug

# Include any dependencies generated for this target.
include src/piframe/CMakeFiles/PiFrame.dir/depend.make

# Include the progress variables for this target.
include src/piframe/CMakeFiles/PiFrame.dir/progress.make

# Include the compile flags for this target's objects.
include src/piframe/CMakeFiles/PiFrame.dir/flags.make

src/piframe/CMakeFiles/PiFrame.dir/main.cpp.o: src/piframe/CMakeFiles/PiFrame.dir/flags.make
src/piframe/CMakeFiles/PiFrame.dir/main.cpp.o: ../../src/piframe/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/CameraCapture/build/Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/piframe/CMakeFiles/PiFrame.dir/main.cpp.o"
	cd /home/pi/CameraCapture/build/Debug/src/piframe && /usr/bin/arm-linux-gnueabihf-g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/PiFrame.dir/main.cpp.o -c /home/pi/CameraCapture/src/piframe/main.cpp

src/piframe/CMakeFiles/PiFrame.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/PiFrame.dir/main.cpp.i"
	cd /home/pi/CameraCapture/build/Debug/src/piframe && /usr/bin/arm-linux-gnueabihf-g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/CameraCapture/src/piframe/main.cpp > CMakeFiles/PiFrame.dir/main.cpp.i

src/piframe/CMakeFiles/PiFrame.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/PiFrame.dir/main.cpp.s"
	cd /home/pi/CameraCapture/build/Debug/src/piframe && /usr/bin/arm-linux-gnueabihf-g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/CameraCapture/src/piframe/main.cpp -o CMakeFiles/PiFrame.dir/main.cpp.s

# Object files for target PiFrame
PiFrame_OBJECTS = \
"CMakeFiles/PiFrame.dir/main.cpp.o"

# External object files for target PiFrame
PiFrame_EXTERNAL_OBJECTS =

bin/PiFrame: src/piframe/CMakeFiles/PiFrame.dir/main.cpp.o
bin/PiFrame: src/piframe/CMakeFiles/PiFrame.dir/build.make
bin/PiFrame: src/piframe/CMakeFiles/PiFrame.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/CameraCapture/build/Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/PiFrame"
	cd /home/pi/CameraCapture/build/Debug/src/piframe && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PiFrame.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/piframe/CMakeFiles/PiFrame.dir/build: bin/PiFrame

.PHONY : src/piframe/CMakeFiles/PiFrame.dir/build

src/piframe/CMakeFiles/PiFrame.dir/clean:
	cd /home/pi/CameraCapture/build/Debug/src/piframe && $(CMAKE_COMMAND) -P CMakeFiles/PiFrame.dir/cmake_clean.cmake
.PHONY : src/piframe/CMakeFiles/PiFrame.dir/clean

src/piframe/CMakeFiles/PiFrame.dir/depend:
	cd /home/pi/CameraCapture/build/Debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/CameraCapture /home/pi/CameraCapture/src/piframe /home/pi/CameraCapture/build/Debug /home/pi/CameraCapture/build/Debug/src/piframe /home/pi/CameraCapture/build/Debug/src/piframe/CMakeFiles/PiFrame.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/piframe/CMakeFiles/PiFrame.dir/depend

