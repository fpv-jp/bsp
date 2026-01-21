#!/bin/bash
# Wi-Fi Base Configuration
# Common functions for SoftAP and Wi-Fi Direct setups
# This file is sourced by other scripts

set -e

# =============================================================================
# NIC Detection
# =============================================================================

# Detect wireless interface (supports various naming conventions)
# Priority: wlan0 > wlan* > wlo* > wlp* > wlx*
detect_wifi_interface() {
  local iface=""

  # Check for common interface names in order of preference
  for pattern in wlan0 "wlan[0-9]*" "wlo[0-9]*" "wlp*" "wlx*"; do
    for path in /sys/class/net/$pattern; do
      if [[ -d "$path/wireless" ]]; then
        iface=$(basename "$path")
        echo "$iface"
        return 0
      fi
    done
  done

  echo ""
  return 1
}

# Get all wireless interfaces
list_wifi_interfaces() {
  for path in /sys/class/net/*/wireless; do
    [[ -d "$path" ]] && basename "$(dirname "$path")"
  done
}

# =============================================================================
# NetworkManager Exclusion
# =============================================================================

# Remove Wi-Fi from NetworkManager management
# This prevents NM from interfering with channel, connection, etc.
exclude_wifi_from_nm() {
  local interfaces="${1:-wl*}"

  echo "Excluding Wi-Fi interfaces from NetworkManager..."

  sudo tee /etc/NetworkManager/conf.d/unmanaged-wifi.conf >/dev/null <<EOF
[keyfile]
unmanaged-devices=interface-name:${interfaces};interface-name:p2p-*
EOF

  sudo systemctl restart NetworkManager
  echo "NetworkManager restarted. Checking device status..."
  nmcli device status
}

# =============================================================================
# Service Management
# =============================================================================

# Mask conflicting services
mask_conflicting_services() {
  echo "Masking conflicting services..."

  # Default wpa_supplicant (conflicts with per-interface service)
  sudo systemctl stop wpa_supplicant.service 2>/dev/null || true
  sudo systemctl mask wpa_supplicant.service

  # hostapd-network if exists
  if systemctl list-unit-files | grep -q hostapd-network; then
    sudo systemctl stop hostapd-network.service 2>/dev/null || true
    sudo systemctl mask hostapd-network.service
  fi
}

# =============================================================================
# Utility Functions
# =============================================================================

# Check if running as root or with sudo
check_privileges() {
  if [[ $EUID -ne 0 ]] && ! sudo -n true 2>/dev/null; then
    echo "This script requires root privileges."
    exit 1
  fi
}

# Get P2P interface name from base interface
get_p2p_interface() {
  local base="$1"
  for path in /sys/class/net/p2p-"${base}"-*; do
    [[ -d "$path" ]] && basename "$path" && return 0
  done
  echo ""
}

# Print configuration summary
print_config() {
  echo "========================================"
  echo "Wi-Fi Interface: ${WIFI_IFACE:-not set}"
  echo "Mode: ${WIFI_MODE:-not set}"
  echo "========================================"
}
