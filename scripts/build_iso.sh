#!/usr/bin/env bash
# ==============================================================================
# Yumemiro OS ISO Build Pipeline Script (Linux / mkarchiso)
# ==============================================================================

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHISO_DIR="$PROJECT_DIR/archiso"
BUILD_DIR="$PROJECT_DIR/build"
WORK_DIR="/tmp/yumemiro-build-work"

echo "=========================================="
echo "🌸 Building Yumemiro OS ISO Image..."
echo "=========================================="

# 1. Run sync to ensure airootfs overlay is up-to-date
python3 "$PROJECT_DIR/scripts/sync_airootfs.py"

# 2. Prepare build output directory
mkdir -p "$BUILD_DIR"
rm -rf "$WORK_DIR"

# 3. Check for mkarchiso tool
if command -v mkarchiso &> /dev/null; then
    echo "Running mkarchiso build..."
    sudo mkarchiso -v -w "$WORK_DIR" -o "$BUILD_DIR" "$ARCHISO_DIR"
    echo "🌸 Yumemiro OS ISO build completed successfully in $BUILD_DIR!"
else
    echo "mkarchiso tool not found in current shell environment."
    echo "If running in standalone mode, use build_iso.py to package distribution overlay."
fi
