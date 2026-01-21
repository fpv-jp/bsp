#!/bin/bash
# GStreamer build for Linux x86-64 with VA-API (AMD/Intel)
# Hardware: VA-API (works with AMD and Intel integrated/discrete GPUs)

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "Linux x86-64 (VA-API)" \
  -Dvaapi=disabled \
  -Dgst-plugins-bad:va=enabled
