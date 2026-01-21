#!/bin/bash
# GStreamer build for Jetson Nano 2GB Devkit
# Hardware: NVIDIA V4L2 API (nvv4l2decoder/nvv4l2h264enc)

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Jetson Nano 2GB Devkit" \
  -Dgst-plugins-bad:v4l2codecs=enabled \
  -Dgst-plugins-bad:nvcodec=disabled \
  -Dgst-plugins-bad:va=disabled
