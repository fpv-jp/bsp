#!/bin/bash
# Wi-Fi Direct (P2P) - Aircraft (Client)
# Uses wpa_supplicant P2P mode as client

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/wifi-base.sh"

# =============================================================================
# Configuration
# =============================================================================

WIFI_IFACE="${WIFI_IFACE:-$(detect_wifi_interface)}"
WIFI_MODE="P2P Client (Aircraft)"

P2P_DEVICE_NAME="${P2P_DEVICE_NAME:-P2P-Aircraft}"
P2P_IP="${P2P_IP:-192.168.49.2}"
P2P_NETMASK="${P2P_NETMASK:-24}"
P2P_GO_MAC="${P2P_GO_MAC:-}"  # Set this to auto-connect

# =============================================================================
# Setup Functions
# =============================================================================

setup_wpa_supplicant() {
  echo "Configuring wpa_supplicant for P2P client mode..."

  local conf_path="/etc/wpa_supplicant/wpa_supplicant-${WIFI_IFACE}.conf"

  sudo tee "$conf_path" >/dev/null <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
device_name=${P2P_DEVICE_NAME}
device_type=1-0050F204-1
p2p_go_intent=0
config_methods=virtual_push_button physical_display keypad
EOF
}

enable_services() {
  echo "Enabling and starting wpa_supplicant..."

  sudo systemctl daemon-reload
  sudo systemctl enable "wpa_supplicant@${WIFI_IFACE}.service"
  sudo systemctl restart "wpa_supplicant@${WIFI_IFACE}.service"
}

find_and_connect() {
  echo "Searching for P2P Group Owners..."

  # Reset P2P state
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_cancel 2>/dev/null || true
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_stop_find 2>/dev/null || true
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_flush 2>/dev/null || true

  sleep 1

  # Start discovery
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_find

  echo "Waiting for discovery (5 seconds)..."
  sleep 5

  # List discovered peers
  echo ""
  echo "Discovered P2P peers:"
  sudo wpa_cli -i "${WIFI_IFACE}" p2p_peers

  if [[ -n "$P2P_GO_MAC" ]]; then
    echo ""
    echo "Auto-connecting to: ${P2P_GO_MAC}"
    sudo wpa_cli -i "${WIFI_IFACE}" p2p_connect "${P2P_GO_MAC}" pbc join
  fi
}

show_status() {
  echo ""
  echo "========================================"
  echo "P2P Client Configuration Complete"
  echo "========================================"
  echo "Device Name: ${P2P_DEVICE_NAME}"
  echo "Interface:   ${WIFI_IFACE}"
  echo "========================================"
  echo ""
  echo "Next steps:"
  echo "  1. Find GO:    sudo wpa_cli -i ${WIFI_IFACE} p2p_peers"
  echo "  2. Connect:    sudo wpa_cli -i ${WIFI_IFACE} p2p_connect <GO_MAC> pbc join"
  echo "  3. Wait for GO to accept PBC"
  echo "  4. Assign IP:  sudo ip addr add ${P2P_IP}/${P2P_NETMASK} dev p2p-${WIFI_IFACE}-0"
  echo "  5. Test:       ping 192.168.49.1"
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
  find_and_connect
  show_status
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
