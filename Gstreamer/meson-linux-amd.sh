#!/bin/bash
# GStreamer build for Linux x86-64 with AMD GPU (AMF)
# Hardware: AMD AMF encoder
#
# Prerequisites:
#   git clone https://github.com/GPUOpen-LibrariesAndSDKs/AMF.git
#   cd AMF/amf/public/include
#   sudo cp -r components core /usr/include/

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Linux x86-64 (AMD AMF)" \
  -Dvaapi=disabled \
  -Dgst-plugins-bad:amfcodec=enabled
