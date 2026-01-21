#!/bin/bash
# GStreamer build for Radxa Rock 5 series
# Hardware: Rockchip MPP (Media Process Platform)
# Note: Requires rockchip-mpp library

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Radxa Rock5" \
  -Dgst-plugins-bad:v4l2codecs=enabled \
  -Dgst-plugins-bad:nvcodec=disabled \
  -Dgst-plugins-bad:va=disabled
