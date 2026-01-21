#!/bin/bash
# GStreamer build for Raspberry Pi 5
# Hardware: openh264 (software codec)

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Raspberry Pi 5" \
  -Dgst-plugins-bad:openh264=enabled \
  -Dgst-plugins-bad:v4l2codecs=disabled \
  -Dgst-plugins-bad:nvcodec=disabled \
  -Dgst-plugins-bad:va=disabled
