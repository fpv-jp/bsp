#!/bin/bash
# SoftAP Mode - Aircraft (Client connecting to AP)
# Uses wpa_supplicant to connect to ground station's AP

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/wifi-base.sh"

# =============================================================================
# Configuration
# =============================================================================

WIFI_IFACE="${WIFI_IFACE:-$(detect_wifi_interface)}"
WIFI_MODE="SoftAP Client (Aircraft)"

AP_SSID="${AP_SSID:-AP-GroundStation}"
AP_PASS="${AP_PASS:-AP-GroundStation}"
CLIENT_IP="${CLIENT_IP:-192.168.50.2}"
CLIENT_NETMASK="${CLIENT_NETMASK:-24}"

# =============================================================================
# Setup Functions
# =============================================================================

setup_wpa_supplicant() {
  echo "Configuring wpa_supplicant for ${WIFI_IFACE}..."

  local conf_path="/etc/wpa_supplicant/wpa_supplicant-${WIFI_IFACE}.conf"

  # Create base config
  sudo tee "$conf_path" >/dev/null <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
EOF

  # Append network config with encrypted passphrase
  wpa_passphrase "${AP_SSID}" "${AP_PASS}" | sudo tee -a "$conf_path" >/dev/null

  # Detect ip command path
  local ip_cmd="/usr/sbin/ip"
  [[ -x "/sbin/ip" ]] && ip_cmd="/sbin/ip"

  # Create systemd override for IP assignment
  sudo mkdir -p "/etc/systemd/system/wpa_supplicant@${WIFI_IFACE}.service.d"
  sudo tee "/etc/systemd/system/wpa_supplicant@${WIFI_IFACE}.service.d/override.conf" >/dev/null <<EOF
[Service]
ExecStartPost=/bin/sleep 2
ExecStartPost=${ip_cmd} addr replace ${CLIENT_IP}/${CLIENT_NETMASK} dev ${WIFI_IFACE}
EOF
}

enable_services() {
  echo "Enabling and starting wpa_supplicant..."

  sudo systemctl daemon-reload
  sudo systemctl enable "wpa_supplicant@${WIFI_IFACE}.service"
  sudo systemctl restart "wpa_supplicant@${WIFI_IFACE}.service"
}

show_status() {
  echo ""
  echo "========================================"
  echo "SoftAP Client Configuration Complete"
  echo "========================================"
  echo "Target SSID: ${AP_SSID}"
  echo "Interface:   ${WIFI_IFACE}"
  echo "IP:          ${CLIENT_IP}/${CLIENT_NETMASK}"
  echo "========================================"
  echo ""

  sudo systemctl status "wpa_supplicant@${WIFI_IFACE}.service" --no-pager || true

  echo ""
  echo "Testing connectivity to ground station..."
  ping -c 3 192.168.50.1 || echo "Ground station not reachable yet."
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
  show_status
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
