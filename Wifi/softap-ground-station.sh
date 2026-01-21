#!/bin/bash
# SoftAP Mode - Ground Station (Access Point)
# Uses hostapd + dnsmasq to create a Wi-Fi access point

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/wifi-base.sh"

# =============================================================================
# Configuration
# =============================================================================

WIFI_IFACE="${WIFI_IFACE:-$(detect_wifi_interface)}"
WIFI_MODE="SoftAP (Ground Station)"

AP_SSID="${AP_SSID:-AP-GroundStation}"
AP_PASS="${AP_PASS:-AP-GroundStation}"
AP_CHANNEL="${AP_CHANNEL:-6}"
AP_IP="${AP_IP:-192.168.50.1}"
AP_NETMASK="${AP_NETMASK:-24}"
AP_DHCP_START="${AP_DHCP_START:-192.168.50.2}"
AP_DHCP_END="${AP_DHCP_END:-192.168.50.16}"

# =============================================================================
# Setup Functions
# =============================================================================

setup_hostapd() {
  echo "Installing and configuring hostapd..."

  sudo apt install -y hostapd
  sudo systemctl unmask hostapd.service

  sudo tee /etc/hostapd/hostapd.conf >/dev/null <<EOF
interface=${WIFI_IFACE}
driver=nl80211
ssid=${AP_SSID}
hw_mode=g
channel=${AP_CHANNEL}
ieee80211n=1
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=${AP_PASS}
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF

  # Set config path
  sudo sed -i 's/^#DAEMON_CONF=.*/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/' /etc/default/hostapd

  # Detect ip command path (differs between distros)
  local ip_cmd="/usr/sbin/ip"
  [[ -x "/sbin/ip" ]] && ip_cmd="/sbin/ip"

  # Create systemd override for IP assignment
  sudo mkdir -p /etc/systemd/system/hostapd.service.d
  sudo tee /etc/systemd/system/hostapd.service.d/override.conf >/dev/null <<EOF
[Service]
ExecStartPost=/bin/sleep 2
ExecStartPost=${ip_cmd} addr replace ${AP_IP}/${AP_NETMASK} dev ${WIFI_IFACE}
Environment=DAEMON_OPTS=

[Unit]
Before=dnsmasq.service
EOF
}

setup_dnsmasq() {
  echo "Installing and configuring dnsmasq..."

  sudo apt install -y dnsmasq
  sudo systemctl unmask dnsmasq.service

  # port=0 disables DNS (let systemd-resolved handle it)
  sudo tee /etc/dnsmasq.conf >/dev/null <<EOF
interface=${WIFI_IFACE}
bind-interfaces
dhcp-range=${AP_DHCP_START},${AP_DHCP_END},255.255.255.0,12h
dhcp-option=3,${AP_IP}
port=0
EOF
}

enable_services() {
  echo "Enabling and starting services..."

  sudo systemctl daemon-reload
  sudo systemctl enable hostapd.service dnsmasq.service
  sudo systemctl restart hostapd.service
  sudo systemctl restart dnsmasq.service
}

show_status() {
  echo ""
  echo "========================================"
  echo "SoftAP Configuration Complete"
  echo "========================================"
  echo "SSID:     ${AP_SSID}"
  echo "Password: ${AP_PASS}"
  echo "Channel:  ${AP_CHANNEL}"
  echo "IP:       ${AP_IP}/${AP_NETMASK}"
  echo "DHCP:     ${AP_DHCP_START} - ${AP_DHCP_END}"
  echo "========================================"
  echo ""

  sudo systemctl status hostapd.service --no-pager || true
  sudo systemctl status dnsmasq.service --no-pager || true
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
  setup_hostapd
  setup_dnsmasq
  enable_services
  show_status
}

# Run if executed directly (not sourced)
[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"
