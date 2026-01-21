1. Install latest cmake
------------------

cd /tmp
wget https://github.com/Kitware/CMake/releases/download/v3.31.11/cmake-3.31.11-linux-aarch64.sh

chmod +x cmake-3.31.11-linux-aarch64.sh
sudo ./cmake-3.31.11-linux-aarch64.sh --skip-license --prefix=/usr/local


2. Install latest Python
------------------
cd
curl -fsSL https://pyenv.run | bash

sudo apt install -y \
  build-essential \
  libbz2-dev \
  libncurses-dev \
  libreadline-dev \
  libssl-dev \
  libffi-dev \
  libsqlite3-dev \
  zlib1g-dev \
  liblzma-dev \
  tk-dev \
  uuid-dev

pyenv install 3.14.2 # takes a while
pyenv shell 3.14.2


3. Clone latest GStreamer
------------------
cd
git clone --branch 1.28.0 --depth 1 https://gitlab.freedesktop.org/gstreamer/gstreamer.git
cd gstreamer


4. Setup venv with latest meson and ninja
------------------
python3 -m venv meson-venv
. meson-venv/bin/activate
pip install --upgrade pip && pip install meson ninja


5. Install common dependencies
------------------
sudo apt install -y \
  curl git bear \
  flex bison valgrind \
  v4l-utils ethtool \
  libdrm-dev libva-dev libgsl-dev \
  libasound2-dev libopus-dev \
  libssl-dev libnsl-dev \
  libjson-glib-dev \
  libnice-dev libsrtp2-dev \
  libdbus-1-dev \
  libelf-dev \
  libinotifytools0-dev \
  libpcre2-dev \
  libvpx-dev libx265-dev \
  libudev-dev libgudev-1.0-dev

# For jetson-nano-2gb-devkit
sudo apt install -y libsoup2.4-dev
# For all other targets
sudo apt install -y libsoup-3.0-dev


6. Run meson for your target
------------------
./meson-raspberry-pi5.sh       # Raspberry Pi 5 (openh264)
./meson-raspberry-pi4.sh       # Raspberry Pi 4 (V4L2)
./meson-jetson-nano-2gb.sh     # Jetson Nano 2GB (NVIDIA V4L2)
./meson-jetson-orin-nano.sh    # Jetson Orin Nano Super
./meson-radxa-rock5.sh         # Radxa Rock 5 (Rockchip MPP)
./meson-linux-amd.sh           # Linux x86-64 (AMD AMF)
./meson-linux-nvidia.sh        # Linux x86-64 (NVIDIA)
./meson-linux-va.sh            # Linux x86-64 (VA-API: AMD/Intel)


7. Build
------------------
ninja -C build -j$(nproc) # takes a while


8. Install (overwrite system packages)
------------------
rm -rf ~/.cache/gstreamer-1.0/
sudo $(pwd)/meson-venv/bin/ninja -C $(pwd)/build install
sudo ldconfig


9. Verify installation
------------------
gst-device-monitor-1.0 --version
