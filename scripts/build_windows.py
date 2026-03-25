# Windows Build Script

# This script is used to build the project on Windows.

setlocal

REM Set environment variables
set BUILD_DIR=build
set SOURCE_DIR=src

REM Create build directory if it doesn't exist
if not exist %BUILD_DIR% (
    mkdir %BUILD_DIR%
)

REM Change to build directory
cd %BUILD_DIR%

REM Run CMake to configure the build
cmake ..\%SOURCE_DIR% -G "Visual Studio 16 2019"

REM Build the project
cmake --build . --config Release

endlocal