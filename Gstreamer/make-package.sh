#!/bin/bash
# GStreamer package builder for SBCs
# Auto-detects device model from /proc/device-tree/model

set -e

GSTREAMER_VERSION="1.28.0"
PACKAGE_ITERATION="1"
MAINTAINER="hexaforce <fpv@fpv.jp>"
VENDOR="FPV Japan"

# Detect device model
detect_device() {
  if [[ -f /proc/device-tree/model ]]; then
    cat /proc/device-tree/model | tr -d '\0'
  else
    echo "unknown"
  fi
}

# Get package name and description based on device model
get_package_info() {
  local model="$1"

  case "$model" in
    *"Raspberry Pi 5"*)
      PACKAGE_NAME="gstreamer-raspberry-pi5"
      PACKAGE_DESC="Raspberry Pi 5"
      ;;
    *"Raspberry Pi 4"*)
      PACKAGE_NAME="gstreamer-raspberry-pi4"
      PACKAGE_DESC="Raspberry Pi 4"
      ;;
    *"Raspberry Pi"*)
      PACKAGE_NAME="gstreamer-raspberry-pi"
      PACKAGE_DESC="Raspberry Pi"
      ;;
    *"NVIDIA Orin Nano"*)
      PACKAGE_NAME="gstreamer-jetson-orin-nano"
      PACKAGE_DESC="Jetson Orin Nano"
      ;;
    *"NVIDIA Jetson Nano 2GB"*)
      PACKAGE_NAME="gstreamer-jetson-nano-2gb"
      PACKAGE_DESC="Jetson Nano 2GB Devkit"
      ;;
    *"Jetson"*|*"NVIDIA"*)
      PACKAGE_NAME="gstreamer-jetson"
      PACKAGE_DESC="NVIDIA Jetson"
      ;;
    *"Radxa"*"ROCK 5"*|*"Rock 5"*)
      PACKAGE_NAME="gstreamer-radxa-rock5"
      PACKAGE_DESC="Radxa Rock 5"
      ;;
    *"Radxa"*|*"Rock"*)
      PACKAGE_NAME="gstreamer-radxa"
      PACKAGE_DESC="Radxa"
      ;;
    *)
      echo "Error: Unknown device model: $model"
      echo "Supported SBCs:"
      echo "  - Raspberry Pi 4/5"
      echo "  - Jetson Nano 2GB / Orin Nano"
      echo "  - Radxa Rock 5"
      exit 1
      ;;
  esac
}

# Detect architecture
detect_arch() {
  local arch=$(uname -m)
  case "$arch" in
    aarch64) echo "arm64" ;;
    armv7l)  echo "armhf" ;;
    *)       echo "$arch" ;;
  esac
}

# Main
DEVICE_MODEL=$(detect_device)
get_package_info "$DEVICE_MODEL"
ARCH=$(detect_arch)

echo "========================================"
echo "Device Model: $DEVICE_MODEL"
echo "Package Name: $PACKAGE_NAME"
echo "Architecture: $ARCH"
echo "========================================"

# Prepare package root
sudo chown -R "$USER:$USER" build/
rm -rf package-root
DESTDIR="$PWD/package-root" ninja -C build install

# Build .deb package
fpm -s dir -t deb \
  -n "$PACKAGE_NAME" \
  -v "$GSTREAMER_VERSION" \
  --iteration "$PACKAGE_ITERATION" \
  --architecture "$ARCH" \
  --prefix=/ \
  --maintainer "$MAINTAINER" \
  --vendor "$VENDOR" \
  --description "GStreamer $GSTREAMER_VERSION for $PACKAGE_DESC ($DEVICE_MODEL)" \
  --url "https://gstreamer.freedesktop.org/" \
  --license "LGPL-2.1" \
  --category multimedia \
  --depends "libasound2" \
  --depends "libnice10" \
  --depends "libsrtp2-1" \
  --depends "libssl3" \
  --depends "libopus0" \
  -C package-root \
  usr

echo "========================================"
echo "Package created: ${PACKAGE_NAME}_${GSTREAMER_VERSION}-${PACKAGE_ITERATION}_${ARCH}.deb"
echo "========================================"
