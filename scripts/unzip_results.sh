#!/bin/bash

# Check if a directory is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Assign the provided directory to a variable
PARENT_DIR="$1"

# Check if the provided argument is a directory
if [ ! -d "$PARENT_DIR" ]; then
  echo "Error: $PARENT_DIR is not a directory."
  exit 1
fi

# Change to the parent directory
cd "$PARENT_DIR" || exit

# Loop through all tar.gz files
for tar_file in *.tar.gz; do
  # Check if there are any tar.gz files
  if [ -e "$tar_file" ]; then
    # Extract the tar.gz file
    tar xf "$tar_file"
    echo "Unzipped $tar_file"
  else
    echo "No .tar.gz files found in $PARENT_DIR"
    break
  fi
done