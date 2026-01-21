# GStreamer Build for FPV Systems

Custom GStreamer build scripts optimized for WebRTC streaming on various SBCs and Linux systems.

## Overview

Minimal GStreamer build with WebRTC stack and hardware-accelerated video encoding where available.

## Supported Platforms

| Platform | Hardware Acceleration | Script |
|----------|----------------------|--------|
| Raspberry Pi 5 | openh264 | `meson-raspberry-pi5.sh` |
| Raspberry Pi 4 | V4L2 API | `meson-raspberry-pi4.sh` |
| Jetson Nano 2GB | NVIDIA V4L2 API | `meson-jetson-nano-2gb.sh` |
| Jetson Orin Nano | openh264, x265, vpx | `meson-jetson-orin-nano.sh` |
| Radxa Rock 5 | Rockchip MPP | `meson-radxa-rock5.sh` |
| Linux x86-64 (AMD) | AMF encoder | `meson-linux-amd.sh` |
| Linux x86-64 (NVIDIA) | NVENC/NVDEC | `meson-linux-nvidia.sh` |
| Linux x86-64 (Intel/AMD) | VA-API | `meson-linux-va.sh` |

## File Structure

```
Gstreamer/
├── install-gstreamer.sh      # Step-by-step build instructions
├── meson-base.sh             # Common meson options (sourced by others)
├── meson-raspberry-pi5.sh    # Raspberry Pi 5 (openh264)
├── meson-raspberry-pi4.sh    # Raspberry Pi 4 (V4L2)
├── meson-jetson-nano-2gb.sh  # Jetson Nano 2GB (NVIDIA V4L2)
├── meson-jetson-orin-nano.sh # Jetson Orin Nano Super
├── meson-radxa-rock5.sh      # Radxa Rock 5 (Rockchip MPP)
├── meson-linux-amd.sh        # Linux x86-64 with AMD GPU
├── meson-linux-nvidia.sh     # Linux x86-64 with NVIDIA GPU
├── meson-linux-va.sh         # Linux x86-64 with VA-API
└── make-package.sh           # Create .deb package (SBCs only)
```

## Quick Start

Follow the steps in `install-gstreamer.sh`:

```bash
# 1. Clone GStreamer
cd ~
git clone --branch 1.28.0 --depth 1 https://gitlab.freedesktop.org/gstreamer/gstreamer.git
cd gstreamer

# 2. Setup Python venv with meson/ninja
python3 -m venv meson-venv
. meson-venv/bin/activate
pip install --upgrade pip && pip install meson ninja

# 3. Install dependencies
sudo apt install -y \
  flex bison libdrm-dev libva-dev \
  libasound2-dev libopus-dev libssl-dev \
  libnice-dev libsrtp2-dev libvpx-dev libx265-dev

# 4. Run meson for your platform
./meson-raspberry-pi5.sh   # or other platform script

# 5. Build
ninja -C build -j$(nproc)

# 6. Install
sudo $(pwd)/meson-venv/bin/ninja -C $(pwd)/build install
sudo ldconfig

# 7. Verify
gst-device-monitor-1.0 --version
```

## Platform Details

### Raspberry Pi 5
- **Codec**: openh264 (software)
- **Note**: BCM2712 does not expose hardware codec via V4L2

### Raspberry Pi 4
- **Codec**: V4L2 stateless codecs
- **Elements**: `v4l2slh264dec`, `v4l2slh264enc`

### Jetson Nano 2GB
- **Codec**: NVIDIA V4L2 API
- **Elements**: `nvv4l2decoder`, `nvv4l2h264enc`
- **Note**: Uses NVIDIA's proprietary V4L2 implementation

### Radxa Rock 5
- **Codec**: Rockchip MPP (Media Process Platform)
- **Prerequisite**: Install `rockchip-mpp` library
- **Elements**: Uses V4L2 with MPP backend

## Enabled Plugins

### Core

| Plugin | Description |
|--------|-------------|
| `app` | appsrc/appsink for application integration |
| `audioconvert` | Audio format conversion |
| `audioresample` | Audio resampling |
| `videoconvertscale` | Video format conversion and scaling |
| `videorate` | Frame rate adjustment |

### Audio

| Plugin | Description |
|--------|-------------|
| `alsa` | ALSA audio input/output |
| `opus` | Opus audio codec |
| `audioparsers` | Audio stream parsers |

### Video

| Plugin | Description |
|--------|-------------|
| `v4l2` | Video4Linux2 camera input |
| `videoparsers` | Video stream parsers (H.264, H.265, etc.) |
| `v4l2codecs` | V4L2 stateless codecs (Pi 4, Jetson, Rock5) |
| `openh264` | OpenH264 software codec (Pi 5, Orin Nano) |
| `nvcodec` | NVIDIA NVENC/NVDEC (Linux NVIDIA) |
| `va` | VA-API hardware acceleration (Intel/AMD) |
| `amfcodec` | AMD AMF encoder (Linux AMD) |

### WebRTC Stack

| Plugin | Description |
|--------|-------------|
| `webrtc` | WebRTC bin element |
| `dtls` | DTLS encryption |
| `srtp` | SRTP encryption |
| `sctp` | SCTP data channels |
| `rtp` | RTP payloading |
| `rtpmanager` | RTP session management |
| `udp` | UDP sink/source |
| `libnice` | ICE connectivity |

## Platform-Specific Prerequisites

### Radxa Rock 5 (Rockchip MPP)

```bash
# Install MPP library (check your distro's package manager)
sudo apt install rockchip-mpp
```

### Linux x86-64 (AMD AMF)

```bash
git clone https://github.com/GPUOpen-LibrariesAndSDKs/AMF.git
cd AMF/amf/public/include
sudo cp -r components core /usr/include/
```

### Linux x86-64 (NVIDIA)

```bash
git clone https://github.com/FFmpeg/nv-codec-headers.git
cd nv-codec-headers
make && sudo make install
```

## Creating Packages (SBCs Only)

The `make-package.sh` script auto-detects the SBC model and creates a `.deb` package:

```bash
# Install fpm first
sudo gem install --no-document fpm

# Run on the target SBC
./make-package.sh
```

Output example:
```
Device Model: Raspberry Pi 5 Model B Rev 1.0
Package Name: gstreamer-raspberry-pi5
Architecture: arm64

Package created: gstreamer-raspberry-pi5_1.28.0-1_arm64.deb
```

### Supported SBCs for Packaging

| Device | Package Name |
|--------|--------------|
| Raspberry Pi 4 | `gstreamer-raspberry-pi4` |
| Raspberry Pi 5 | `gstreamer-raspberry-pi5` |
| Jetson Nano 2GB | `gstreamer-jetson-nano-2gb` |
| Jetson Orin Nano | `gstreamer-jetson-orin-nano` |
| Radxa Rock 5 | `gstreamer-radxa-rock5` |

## Adding New Platforms

1. Create a new meson script that sources `meson-base.sh`:

```bash
#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/meson-base.sh"

build_gstreamer "My New Platform" \
  -Dgst-plugins-bad:mycodec=enabled \
  -Dgst-plugins-bad:va=disabled
```

2. Add device detection to `make-package.sh` if it's an SBC.

## Troubleshooting

### Check available plugins

```bash
gst-inspect-1.0 | grep -i webrtc
gst-inspect-1.0 | grep -i v4l2
gst-inspect-1.0 | grep -i opus
gst-inspect-1.0 | grep -i openh264
```

### Test camera

```bash
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! autovideosink
```

### Test WebRTC elements

```bash
gst-inspect-1.0 webrtcbin
gst-inspect-1.0 dtlssrtpenc
```

### Clear plugin cache

```bash
rm -rf ~/.cache/gstreamer-1.0/
```
