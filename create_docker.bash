#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Build the Docker image using the determined context
docker build -t reactive-synthesis-lecture-2024 "$SCRIPT_DIR"