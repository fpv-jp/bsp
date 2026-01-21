#!/bin/bash
# GStreamer meson build - Common base configuration
# This file is sourced by target-specific build scripts

# Usage: source this file, then call build_gstreamer with target-specific options
# Example:
#   source meson-base.sh
#   build_gstreamer "Raspberry Pi 4/5" \
#     "-Dgst-plugins-bad:v4l2codecs=enabled"

MESON_BASE_OPTIONS=(
  --prefix=/usr
  -Dbuildtype=release
  -Dauto_features=disabled
  -Dintrospection=disabled
  -Ddoc=disabled
  -Dexamples=disabled
  -Dtests=disabled
  -Dnls=disabled
  -Dtools=enabled
  -Dbase=enabled
  -Dgood=enabled
  -Dbad=enabled
  -Dugly=disabled
  -Dlibav=disabled
  -Dlibnice=enabled
  -Ddevtools=disabled
  -Dpython=disabled
  -Drtsp_server=enabled
  # gstreamer core
  -Dgstreamer:tools=enabled
  -Dgstreamer:check=disabled
  # gst-plugins-base
  -Dgst-plugins-base:alsa=enabled
  -Dgst-plugins-base:opus=enabled
  -Dgst-plugins-base:audioconvert=enabled
  -Dgst-plugins-base:audioresample=enabled
  -Dgst-plugins-base:videorate=enabled
  -Dgst-plugins-base:videoconvertscale=enabled
  -Dgst-plugins-base:rawparse=enabled
  -Dgst-plugins-base:app=enabled
  # gst-plugins-good
  -Dgst-plugins-good:v4l2=enabled
  -Dgst-plugins-good:rtp=enabled
  -Dgst-plugins-good:rtsp=enabled
  -Dgst-plugins-good:rtpmanager=enabled
  -Dgst-plugins-good:udp=enabled
  -Dgst-plugins-good:audioparsers=enabled
  -Dgst-plugins-good:pulse=disabled
  # gst-plugins-bad (WebRTC stack)
  -Dgst-plugins-bad:webrtc=enabled
  -Dgst-plugins-bad:dtls=enabled
  -Dgst-plugins-bad:srtp=enabled
  -Dgst-plugins-bad:sctp=enabled
  -Dgst-plugins-bad:videoparsers=enabled
  -Dgst-plugins-bad:opus=enabled
  # gst-rtsp-server
  -Dgst-rtsp-server:rtspclientsink=enabled
  # libnice
  -Dlibnice:gstreamer=enabled
)

build_gstreamer() {
  local target_name="$1"
  shift
  local extra_options=("$@")

  echo "Building GStreamer for: ${target_name}"
  echo "========================================"

  meson setup build \
    "${MESON_BASE_OPTIONS[@]}" \
    -Dpackage-origin="Built for ${target_name} by FPV Japan" \
    "${extra_options[@]}"
}
