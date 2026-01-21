diff all defaults

# version
# Betaflight / STM32F405 (S405) 4.5.2 Apr 22 2025 / 05:00:37 (024f8e13d) MSP API: 1.46
# config rev: 3029a1e

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name AOCODARCF405V3
manufacturer_id SJET
mcu_id 0040001e3433510939363935
signature 

# resources
#resource MOTOR 5 A15
resource MOTOR 5 NONE
#resource MOTOR 6 A08
resource MOTOR 6 NONE
#resource SERVO 1 NONE
resource SERVO 1 A15
#resource SERVO 2 NONE
resource SERVO 2 A08
#feature -SERVO_TILT
#feature -GPS
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD
#feature -CHANNEL_FORWARDING

# feature
feature SERVO_TILT
feature GPS
feature TELEMETRY
feature LED_STRIP
feature OSD
feature CHANNEL_FORWARDING

# serial
#serial 3 0 115200 57600 0 115200
serial 3 2048 115200 57600 0 115200

# servo
#servo 0 1000 2000 1500 100 -1
servo 0 1000 2000 1500 100 7
#servo 1 1000 2000 1500 100 -1
servo 1 1000 2000 1500 100 8

# led
#led 0 0,0::C:0
led 0 4,5::CO:8
#led 1 0,0::C:0
led 1 5,5::CO:8
#led 2 0,0::C:0
led 2 6,5::CO:8
#led 3 0,0::C:0
led 3 7,5::CO:8
#led 4 0,0::C:0
led 4 8,5::CO:8
#led 5 0,0::C:0
led 5 9,5::CO:8
#led 6 0,0::C:0
led 6 10,5::CO:8
#led 7 0,0::C:0
led 7 11,5::CO:8

# aux
#aux 0 0 0 900 900 0 0
aux 0 0 0 1800 2100 0 0
#aux 1 0 0 900 900 0 0
aux 1 1 2 900 1250 0 0
#aux 2 0 0 900 900 0 0
aux 2 2 2 1300 1700 0 0
#aux 3 0 0 900 900 0 0
aux 3 6 2 1750 2100 0 0
#aux 4 0 0 900 900 0 0
aux 4 13 1 1700 2100 0 0
#aux 5 0 0 900 900 0 0
aux 5 40 3 1000 2000 0 0
#aux 6 0 0 900 900 0 0
aux 6 41 4 1000 2000 0 0

# vtxtable
#vtxtable bands 0
vtxtable bands 5
#vtxtable channels 0
vtxtable channels 8
#vtxtable band 1 BAND1    1 CUSTOM 
vtxtable band 1 BOSCAM_A A FACTORY 5865 5845 5825 5805 5785 5765 5745 5725
#vtxtable band 2 BAND2    2 CUSTOM 
vtxtable band 2 BOSCAM_B B FACTORY 5733 5752 5771 5790 5809 5828 5847 5866
#vtxtable band 3 BAND3    3 CUSTOM 
vtxtable band 3 BOSCAM_E E FACTORY 5705 5685 5665    0 5885 5905    0    0
#vtxtable band 4 BAND4    4 CUSTOM 
vtxtable band 4 FATSHARK F FACTORY 5740 5760 5780 5800 5820 5840 5860 5880
#vtxtable band 5 BAND5    5 CUSTOM 
vtxtable band 5 RACEBAND R FACTORY 5658 5695 5732 5769 5806 5843 5880 5917
#vtxtable powerlevels 0
vtxtable powerlevels 4
#vtxtable powervalues 0 0 0 0 0 0 0 0
vtxtable powervalues 0 1 2 3
#vtxtable powerlabels LV0 LV1 LV2 LV3 LV4 LV5 LV6 LV7
vtxtable powerlabels 25 200 600 120

# master
#set acc_trim_pitch = 0
set acc_trim_pitch = 1
#set acc_calibration = 0,0,0,0
set acc_calibration = -33,12,32,1
#set baro_i2c_address = 0
set baro_i2c_address = 118
#set baro_hardware = AUTO
set baro_hardware = DPS310
#set osd_vbat_pos = 341
set osd_vbat_pos = 2412
#set osd_rssi_pos = 341
set osd_rssi_pos = 342
#set osd_link_quality_pos = 341
set osd_link_quality_pos = 0
#set osd_link_tx_power_pos = 341
set osd_link_tx_power_pos = 64
#set osd_rssi_dbm_pos = 341
set osd_rssi_dbm_pos = 32
#set osd_tim_2_pos = 341
set osd_tim_2_pos = 407
#set osd_flymode_pos = 341
set osd_flymode_pos = 2432
#set osd_vtx_channel_pos = 341
set osd_vtx_channel_pos = 352
#set osd_crosshairs_pos = 312
set osd_crosshairs_pos = 2253
#set osd_ah_sbar_pos = 313
set osd_ah_sbar_pos = 2254
#set osd_ah_pos = 185
set osd_ah_pos = 2126
#set osd_current_pos = 341
set osd_current_pos = 395
#set osd_mah_drawn_pos = 341
set osd_mah_drawn_pos = 384
#set osd_wh_drawn_pos = 341
set osd_wh_drawn_pos = 405
#set osd_craft_name_pos = 341
set osd_craft_name_pos = 395
#set osd_gps_speed_pos = 341
set osd_gps_speed_pos = 2242
#set osd_gps_lon_pos = 341
set osd_gps_lon_pos = 2112
#set osd_gps_lat_pos = 341
set osd_gps_lat_pos = 2080
#set osd_gps_sats_pos = 341
set osd_gps_sats_pos = 2048
#set osd_home_dir_pos = 341
set osd_home_dir_pos = 2071
#set osd_home_dist_pos = 341
set osd_home_dist_pos = 2072
#set osd_compass_bar_pos = 341
set osd_compass_bar_pos = 2058
#set osd_altitude_pos = 341
set osd_altitude_pos = 2262
#set osd_warnings_pos = 14772
set osd_warnings_pos = 14665
#set osd_avg_cell_voltage_pos = 341
set osd_avg_cell_voltage_pos = 353
#set osd_pit_ang_pos = 341
set osd_pit_ang_pos = 151
#set osd_rol_ang_pos = 341
set osd_rol_ang_pos = 119
#set osd_battery_usage_pos = 341
set osd_battery_usage_pos = 2440
#set osd_disarmed_pos = 341
set osd_disarmed_pos = 2453
#set osd_nheading_pos = 341
set osd_nheading_pos = 12
#set osd_nvario_pos = 341
set osd_nvario_pos = 194
#set osd_sys_bitrate_pos = 341
set osd_sys_bitrate_pos = 0
#set osd_sys_delay_pos = 341
set osd_sys_delay_pos = 64
#set osd_sys_distance_pos = 341
set osd_sys_distance_pos = 64
#set osd_sys_vtx_dvr_pos = 341
set osd_sys_vtx_dvr_pos = 32
#set osd_canvas_width = 53
set osd_canvas_width = 30
#set osd_canvas_height = 20
set osd_canvas_height = 13
#set vtx_band = 0
set vtx_band = 3
#set vtx_channel = 0
set vtx_channel = 5
#set vtx_power = 0
set vtx_power = 1
#set vtx_low_power_disarm = OFF
set vtx_low_power_disarm = ON
#set vtx_freq = 0
set vtx_freq = 5885
#set i2c1_pullup = OFF
set i2c1_pullup = ON

profile 0

profile 1

profile 2

profile 3

# restore original profile selection
profile 0

rateprofile 0

rateprofile 1

rateprofile 2

rateprofile 3

# restore original rateprofile selection
rateprofile 0

# save configuration
save
# 