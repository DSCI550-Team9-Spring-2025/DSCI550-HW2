#!/bin/bash

# Get the current working directory
CURRENT_DIR=$(pwd)

# Define the target directory
TARGET_DIR="$CURRENT_DIR/lucene-geo-gazetteer/src/main/bin"

# Check if TARGET_DIR exists
if [ -d "$TARGET_DIR" ]; then
    # Add TARGET_DIR to PATH if it's not already there
    if [[ ":$PATH:" != *":$TARGET_DIR:"* ]]; then
        export PATH="$TARGET_DIR:$PATH"
        echo "Added $TARGET_DIR to PATH"
    else
        echo "$TARGET_DIR is already in PATH"
    fi
else
    echo "Directory $TARGET_DIR does not exist"
fi
