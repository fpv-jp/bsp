#!/bin/bash
# Wi-Fi Direct (P2P) - Ground Station (Group Owner)
# Uses wpa_supplicant P2P mode as GO

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/wifi-base.sh"

# =============================================================================
# Configuration
# =============================================================================

WIFI_IFACE="${WIFI_IFACE:-$(detect_wifi_interface)}"
WIFI_MODE="P2P Group Owner (Ground Station)"

P2P_DEVICE_NAME="${P2P_DEVICE_NAME:-GO-GroundStation}"
P2P_FREQ="${P2P_FREQ:-2437}"  # Channel 6
P2P_IP="${P2P_IP:-192.168.49.1}"
P2P_NETMASK="${P2P_NETMASK:-24}"

# =============================================================================
# Setup Functions
# =============================================================================

setup_wpa_supplicant() {
  echo "Configuring wpa_supplicant for P2P GO mode..."

  local conf_path="/etc/wpa_supplicant/wpa_supplicant-${WIFI_IFACE}.conf"

  sudo tee "$conf_path" >/dev/null <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
device_name=${P2P_DEVICE_NAME}
device_type=6-0050F204-1
p2p_ssid_postfix=_FPV
config_methods=virtual_push_button physical_display keypad
EOF

  # Create systemd override
  sudo mkdir -p "/etc/systemd/system/wpa_supplicant@${WIFI_IFACE}.service.d"
  sudo tee "/etc/systemd/system/wpa_supplicant@${WIFI_IFACE}.service.d/override.conf" >/dev/null <<EOF
[Service]
ExecStart=
ExecStart=/usr/sbin/wpa_supplicant -Dnl80211 -i${WIFI_IFACE} -c${conf_path}
EOF
}

enable_services() {
  echo "Enabling and starting wpa_supplicant..."

  sudo systemctl daemon-reload
  sudo systemctl enable "wpa_supplicant@${WIFI_IFACE}.service"
  sudo systemctl restart "wpa_supplicant@${WIFI_IFACE}.service"
}

start_p2p_group() {
  echo "Starting P2P Group (GO mode)..."
  echo "Frequency: ${P2P_FREQ} MHz"

  # Reset any existing P2P state
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_cancel 2>/dev/null || true
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_stop_find 2>/dev/null || true
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_flush 2>/dev/null || true

  sleep 1

  # Start P2P Group
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_group_add freq="${P2P_FREQ}"

  echo "Waiting for P2P interface..."
  sleep 3

  local p2p_iface=$(get_p2p_interface "${WIFI_IFACE}")
  if [[ -n "$p2p_iface" ]]; then
    echo "P2P interface created: ${p2p_iface}"
    iw dev "${p2p_iface}" info
  else
    echo "Warning: P2P interface not yet created."
  fi
}

show_status() {
  echo ""
  echo "========================================"
  echo "P2P GO Configuration Complete"
  echo "========================================"
  echo "Device Name: ${P2P_DEVICE_NAME}"
  echo "Interface:   ${WIFI_IFACE}"
  echo "Frequency:   ${P2P_FREQ} MHz"
  echo "========================================"
  echo ""
  echo "Next steps:"
  echo "  1. Wait for client to send PBC request"
  echo "  2. Accept with: sudo wpa_cli -i p2p-${WIFI_IFACE}-0 wps_pbc"
  echo "  3. Assign IP:   sudo ip addr add ${P2P_IP}/${P2P_NETMASK} dev p2p-${WIFI_IFACE}-0"
  echo ""
}

# =============================================================================
# Main
# =============================================================================

main() {
  check_privileges
  print_config

  if [[ -z "$WIFI_IFACE" ]]; then
    echo "Error: No wireless interface detected."
    echo "Available interfaces:"
    list_wifi_interfaces
    exit 1
  fi

  mask_conflicting_services
  exclude_wifi_from_nm "${WIFI_IFACE}"
  setup_wpa_supplicant
  enable_services
  start_p2p_group
  show_status
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
