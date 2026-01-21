diff all defaults

# version
# Betaflight / STM32F405 (S405) 4.5.2 Mar 25 2025 / 13:34:35 (024f8e13d) MSP API: 1.46
# config rev: 48588b7

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name SPEDIXF405
manufacturer_id SPDX
mcu_id 0030001e3133471431353636
signature 

# name: R10
#feature -GPS
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD

# feature
feature GPS
feature TELEMETRY
feature LED_STRIP
feature OSD

# serial
#serial 0 0 115200 57600 0 115200
serial 0 8192 115200 57600 0 115200
#serial 3 0 115200 57600 0 115200
serial 3 2 115200 57600 0 115200

# led
#led 0 0,0::C:0
led 0 0,0::L:0

# aux
#aux 0 0 0 900 900 0 0
aux 0 0 0 1700 2100 0 0
#aux 1 0 0 900 900 0 0
aux 1 1 1 900 1200 0 0
#aux 2 0 0 900 900 0 0
aux 2 2 1 1300 1700 0 0
#aux 3 0 0 900 900 0 0
aux 3 13 2 1700 2100 0 0

# adjrange
#adjrange 0 0 0 900 900 0 0 0 0
adjrange 0 0 0 1000 2000 0 0 0 0

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
vtxtable band 3 BOSCAM_E E CUSTOM  5705 5685 5665 5645 5885 5905 5925 5945
#vtxtable band 4 BAND4    4 CUSTOM 
vtxtable band 4 FATSHARK F CUSTOM  5740 5760 5780 5800 5820 5840 5860 5880
#vtxtable band 5 BAND5    5 CUSTOM 
vtxtable band 5 RACEBAND R CUSTOM  5658 5695 5732 5769 5806 5843 5880 5917
#vtxtable powerlevels 0
vtxtable powerlevels 4
#vtxtable powervalues 0 0 0 0 0 0 0 0
vtxtable powervalues 25 400 800 1600
#vtxtable powerlabels LV0 LV1 LV2 LV3 LV4 LV5 LV6 LV7
vtxtable powerlabels 25 400 800 MAX

# master
#set dyn_notch_count = 3
set dyn_notch_count = 1
#set dyn_notch_q = 300
set dyn_notch_q = 500
#set acc_calibration = 0,0,0,0
set acc_calibration = -1,-2,32,1
#set dshot_bidir = OFF
set dshot_bidir = ON
#set motor_pwm_protocol = DSHOT600
set motor_pwm_protocol = DSHOT300
#set pid_process_denom = 1
set pid_process_denom = 2
#set osd_link_quality_pos = 341
set osd_link_quality_pos = 2272
#set osd_rssi_dbm_pos = 341
set osd_rssi_dbm_pos = 2208
#set osd_rsnr_pos = 341
set osd_rsnr_pos = 2048
#set osd_flymode_pos = 341
set osd_flymode_pos = 2455
#set osd_mah_drawn_pos = 341
set osd_mah_drawn_pos = 2336
#set osd_wh_drawn_pos = 341
set osd_wh_drawn_pos = 2144
#set osd_home_dir_pos = 341
set osd_home_dir_pos = 2072
#set osd_home_dist_pos = 341
set osd_home_dist_pos = 2104
#set osd_warnings_pos = 14772
set osd_warnings_pos = 14697
#set osd_nheading_pos = 341
set osd_nheading_pos = 2168
#set osd_rcchannels_pos = 341
set osd_rcchannels_pos = 2432
#set osd_sys_goggle_voltage_pos = 341
set osd_sys_goggle_voltage_pos = 2112
#set osd_canvas_width = 53
set osd_canvas_width = 30
#set osd_canvas_height = 20
set osd_canvas_height = 13
#set vtx_band = 0
set vtx_band = 1
#set vtx_power = 0
set vtx_power = 2
#set vtx_low_power_disarm = OFF
set vtx_low_power_disarm = ON
#set craft_name = -
set craft_name = R10
#set pilot_name = -
set pilot_name = unknown

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