#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/build"
ZIP_NAME="add_delivery.zip"
ZIP_PATH="${SCRIPT_DIR}/../../${ZIP_NAME}"

rm -rf "$BUILD_DIR"
rm -f "$ZIP_PATH"

mkdir -p "$BUILD_DIR"
pip3 install -r "${SCRIPT_DIR}/requirements.txt" -t "$BUILD_DIR"
cp "${SCRIPT_DIR}/"*.py "$BUILD_DIR"

cd "$BUILD_DIR"
# IMPORTANT: Use this command to zip *contents* of build, NOT the build folder itself
zip -r "$ZIP_PATH" . -x "*__pycache__*"

echo "Lambda package created at $ZIP_PATH"
