#!/bin/bash
# GStreamer build for Raspberry Pi 4
# Hardware: V4L2 stateless codecs

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Raspberry Pi 4" \
  -Dgst-plugins-bad:v4l2codecs=enabled \
  -Dgst-plugins-bad:nvcodec=disabled \
  -Dgst-plugins-bad:va=disabled
