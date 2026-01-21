#!/bin/bash
# GStreamer build for Linux x86-64 with NVIDIA GPU (NVENC/NVDEC)
# Hardware: NVIDIA nvcodec
#
# Prerequisites:
#   git clone https://github.com/FFmpeg/nv-codec-headers.git
#   cd nv-codec-headers
#   make && sudo make install

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Linux x86-64 (NVIDIA)" \
  -Dvaapi=disabled \
  -Dgst-plugins-bad:nvcodec=enabled
