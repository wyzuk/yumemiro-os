#!/usr/bin/env bash

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHISO_DIR="$PROJECT_DIR/archiso"
BUILD_DIR="$PROJECT_DIR/build"
WORK_DIR="/tmp/yumemiro-build-work"

echo "=========================================="
echo "🌸 Building Yumemiro OS ISO Image..."
echo "=========================================="

# Sync airootfs overlay
python3 "$PROJECT_DIR/scripts/sync_airootfs.py"

# Prepare build output directory
mkdir -p "$BUILD_DIR"
rm -rf "$WORK_DIR"

# Check for mkarchiso tool
if command -v mkarchiso &> /dev/null; then
    echo "Running mkarchiso build..."
    sudo mkarchiso -v -w "$WORK_DIR" -o "$BUILD_DIR" "$ARCHISO_DIR"
    echo "🌸 Yumemiro OS ISO build completed successfully in $BUILD_DIR!"
else
    echo "mkarchiso tool not found in current shell environment."
    echo "If running in standalone mode, use build_iso.py to package distribution overlay."
fi
