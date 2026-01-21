diff all defaults

# version
# Betaflight / STM32F745 (S745) 4.5.2 Mar 20 2025 / 19:02:56 (024f8e13d) MSP API: 1.46
# config rev: 3eedb40

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name IFLIGHT_BLITZ_F7_AIO
manufacturer_id IFRC
mcu_id 0048003b5448500620393734
signature 

# name: Protek 35 v2
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD

# feature
feature TELEMETRY
feature LED_STRIP
feature OSD

# serial
#serial 2 0 115200 57600 0 115200
serial 2 64 115200 57600 0 115200
#serial 6 0 115200 57600 0 115200
serial 6 8192 115200 57600 0 115200

# aux
#aux 0 0 0 900 900 0 0
aux 0 0 0 1700 2100 0 0
#aux 1 0 0 900 900 0 0
aux 1 1 1 900 1200 0 0
#aux 2 0 0 900 900 0 0
aux 2 2 1 1300 1700 0 0
#aux 3 0 0 900 900 0 0
aux 3 13 2 1700 2100 0 0

# vtxtable
#vtxtable bands 0
vtxtable bands 5
#vtxtable channels 0
vtxtable channels 8
#vtxtable band 1 BAND1    1 CUSTOM 
vtxtable band 1 BOSCAM_A A CUSTOM  5865 5845 5825 5805 5785 5765 5745 5725
#vtxtable band 2 BAND2    2 CUSTOM 
vtxtable band 2 BOSCAM_B B CUSTOM  5733 5752 5771 5790 5809 5828 5847 5866
#vtxtable band 3 BAND3    3 CUSTOM 
vtxtable band 3 BOSCAM_E E CUSTOM  5705 5685 5665    0 5885 5905    0    0
#vtxtable band 4 BAND4    4 CUSTOM 
vtxtable band 4 FATSHARK F CUSTOM  5740 5760 5780 5800 5820 5840 5860 5880
#vtxtable band 5 BAND5    5 CUSTOM 
vtxtable band 5 RACEBAND R CUSTOM  5658 5695 5732 5769 5806 5843 5880 5917
#vtxtable powerlevels 0
vtxtable powerlevels 4
#vtxtable powervalues 0 0 0 0 0 0 0 0
vtxtable powervalues 25 200 400 600
#vtxtable powerlabels LV0 LV1 LV2 LV3 LV4 LV5 LV6 LV7
vtxtable powerlabels 25 200 400 600

# master
#set acc_calibration = 0,0,0,0
set acc_calibration = -47,17,-10,1
#set min_check = 1050
set min_check = 1000
#set max_check = 1900
set max_check = 2000
#set rssi_channel = 0
set rssi_channel = 5
#set motor_pwm_protocol = DSHOT600
set motor_pwm_protocol = DSHOT300
#set align_board_yaw = 135
set align_board_yaw = 225
#set yaw_motors_reversed = OFF
set yaw_motors_reversed = ON
#set small_angle = 25
set small_angle = 180
#set deadband = 0
set deadband = 1
#set yaw_deadband = 0
set yaw_deadband = 1
#set osd_vbat_pos = 341
set osd_vbat_pos = 2433
#set osd_rssi_pos = 341
set osd_rssi_pos = 342
#set osd_link_quality_pos = 341
set osd_link_quality_pos = 2113
#set osd_rssi_dbm_pos = 341
set osd_rssi_dbm_pos = 299
#set osd_tim_2_pos = 341
set osd_tim_2_pos = 2455
#set osd_flymode_pos = 341
set osd_flymode_pos = 2105
#set osd_vtx_channel_pos = 341
set osd_vtx_channel_pos = 2081
#set osd_current_pos = 341
set osd_current_pos = 352
#set osd_mah_drawn_pos = 341
set osd_mah_drawn_pos = 14720
#set osd_craft_name_pos = 341
set osd_craft_name_pos = 2443
#set osd_warnings_pos = 14772
set osd_warnings_pos = 14666
#set osd_avg_cell_voltage_pos = 341
set osd_avg_cell_voltage_pos = 2401
#set osd_disarmed_pos = 341
set osd_disarmed_pos = 288
#set osd_canvas_width = 53
set osd_canvas_width = 30
#set osd_canvas_height = 20
set osd_canvas_height = 13
#set debug_mode = NONE
set debug_mode = GYRO_SCALED
#set vtx_band = 0
set vtx_band = 3
#set vtx_channel = 0
set vtx_channel = 1
#set vtx_power = 0
set vtx_power = 4
#set vtx_low_power_disarm = OFF
set vtx_low_power_disarm = ON
#set vtx_freq = 0
set vtx_freq = 5705
#set vcd_video_system = HD
set vcd_video_system = NTSC
#set gyro_1_sensor_align = CW0
set gyro_1_sensor_align = DEFAULT
#set gyro_1_align_yaw = 0
set gyro_1_align_yaw = 1800
#set craft_name = -
set craft_name = Protek 35 v2

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