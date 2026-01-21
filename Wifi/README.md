# Wi-Fi Configuration for FPV Systems

Wi-Fi connection setup scripts for ground station and aircraft communication.

## Overview

Two connection methods are available:

| Method | Ground Station | Aircraft | Use Case |
|--------|---------------|----------|----------|
| **SoftAP** | Access Point (hostapd) | Client (wpa_supplicant) | Simple, reliable |
| **Wi-Fi Direct (P2P)** | Group Owner | Client | No AP needed, direct link |

## File Structure

```
Wifi/
├── wifi-base.sh              # Common functions (sourced by other scripts)
├── softap-ground-station.sh  # SoftAP: Ground station as AP
├── softap-aircraft.sh        # SoftAP: Aircraft connects to AP
├── p2p-ground-station.sh     # P2P: Ground station as Group Owner
├── p2p-aircraft.sh           # P2P: Aircraft as client
└── p2p-config-tui.sh         # Interactive TUI for P2P setup
```

## Quick Start

### SoftAP Mode

```bash
# Ground Station (run first)
./softap-ground-station.sh

# Aircraft
./softap-aircraft.sh
```

Default settings:
- SSID: `AP-GroundStation`
- Password: `AP-GroundStation`
- Ground Station IP: `192.168.50.1`
- Aircraft IP: `192.168.50.2`

### Wi-Fi Direct (P2P) Mode

```bash
# Ground Station (run first)
./p2p-ground-station.sh

# Aircraft
./p2p-aircraft.sh

# Then on Ground Station, accept connection:
sudo wpa_cli -i p2p-wlan0-0 wps_pbc

# Assign IPs manually:
# Ground Station
sudo ip addr add 192.168.49.1/24 dev p2p-wlan0-0
# Aircraft
sudo ip addr add 192.168.49.2/24 dev p2p-wlan0-0
```

## Configuration

All scripts support environment variables for customization:

### SoftAP

```bash
# Ground Station
WIFI_IFACE=wlo1 \
AP_SSID=MyDrone \
AP_PASS=secretpass \
AP_CHANNEL=11 \
AP_IP=10.0.0.1 \
./softap-ground-station.sh

# Aircraft
WIFI_IFACE=wlan0 \
AP_SSID=MyDrone \
AP_PASS=secretpass \
CLIENT_IP=10.0.0.2 \
./softap-aircraft.sh
```

### Wi-Fi Direct (P2P)

```bash
# Ground Station
WIFI_IFACE=wlo1 \
P2P_DEVICE_NAME=MyGO \
P2P_FREQ=5180 \
./p2p-ground-station.sh

# Aircraft
WIFI_IFACE=wlan0 \
P2P_DEVICE_NAME=MyAircraft \
P2P_GO_MAC=aa:bb:cc:dd:ee:ff \
./p2p-aircraft.sh
```

### Common Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WIFI_IFACE` | auto-detect | Wi-Fi interface (wlan0, wlo1, etc.) |

### SoftAP Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AP_SSID` | AP-GroundStation | Access point SSID |
| `AP_PASS` | AP-GroundStation | WPA2 password |
| `AP_CHANNEL` | 6 | Wi-Fi channel (1-11 for 2.4GHz) |
| `AP_IP` | 192.168.50.1 | Ground station IP |
| `CLIENT_IP` | 192.168.50.2 | Aircraft IP |

### P2P Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `P2P_DEVICE_NAME` | GO-GroundStation | Device name shown in discovery |
| `P2P_FREQ` | 2437 | Frequency in MHz (2437 = Ch6) |
| `P2P_IP` | 192.168.49.1 | GO IP address |
| `P2P_GO_MAC` | (none) | Auto-connect to this MAC |

## Frequency Reference

### 2.4 GHz

| Channel | Frequency (MHz) |
|---------|-----------------|
| 1 | 2412 |
| 6 | 2437 |
| 11 | 2462 |

### 5 GHz

| Channel | Frequency (MHz) |
|---------|-----------------|
| 36 | 5180 |
| 40 | 5200 |
| 44 | 5220 |
| 48 | 5240 |

## NetworkManager

These scripts automatically exclude Wi-Fi interfaces from NetworkManager to prevent:
- Automatic disconnection
- Channel changes
- Connection attempts to other networks

Configuration is written to `/etc/NetworkManager/conf.d/unmanaged-wifi.conf`.

## Supported NIC Names

The scripts auto-detect interfaces with these naming patterns:
- `wlan0`, `wlan1` - Traditional naming
- `wlo1` - Systemd predictable naming (onboard)
- `wlp2s0` - Systemd predictable naming (PCI)
- `wlx*` - Systemd predictable naming (USB, by MAC)

## Troubleshooting

### Check service status

```bash
# SoftAP
sudo systemctl status hostapd
sudo systemctl status dnsmasq

# P2P / Client
sudo systemctl status wpa_supplicant@wlan0
```

### View logs

```bash
sudo journalctl -u hostapd -f
sudo journalctl -u wpa_supplicant@wlan0 -f
```

### Check interface status

```bash
ip addr show wlan0
iw dev wlan0 info
sudo wpa_cli -i wlan0 status
```

### Reset P2P state

```bash
sudo wpa_cli -i wlan0 p2p_cancel
sudo wpa_cli -i wlan0 p2p_flush
sudo systemctl restart wpa_supplicant@wlan0
```

## Interactive Setup

For step-by-step P2P configuration with a menu interface:

```bash
./p2p-config-tui.sh
```

Requires: `whiptail`
