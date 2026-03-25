#!/bin/bash

# Builds the project for Linux
# Run this script from the root of the repository

echo "Starting build process..."

# Set up environment variables if needed
# export VAR_NAME=value

# Build command
make build-linux

if [ $? -eq 0 ]; then
    echo "Build successful!"
else
    echo "Build failed!"
    exit 1
fi

# Other tasks could be added here
