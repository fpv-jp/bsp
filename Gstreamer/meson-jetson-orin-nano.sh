#!/bin/bash
# GStreamer build for Jetson Orin Nano Super
# Hardware: Software codecs (openh264, x265, vpx)

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Jetson Orin Nano Super" \
  -Dgpl=enabled \
  -Dgst-plugins-good:vpx=enabled \
  -Dgst-plugins-bad:openh264=enabled \
  -Dgst-plugins-bad:x265=enabled \
  -Dgst-plugins-bad:nvcodec=disabled \
  -Dgst-plugins-bad:va=disabled
