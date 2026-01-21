diff all defaults

# version
# Betaflight / STM32F745 (S745) 4.5.2 Mar 21 2025 / 20:52:47 (024f8e13d) MSP API: 1.46
# config rev: 3eedb40

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name IFLIGHT_F745_AIO_V2
manufacturer_id IFRC
mcu_id 004f00295030500720323530
signature 

# name: Protek 35
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD

# feature
feature TELEMETRY
feature LED_STRIP
feature OSD

# serial
#serial 0 0 115200 57600 0 115200
serial 0 64 115200 57600 0 115200
#serial 6 0 115200 57600 0 115200
serial 6 8192 115200 57600 0 115200
#beacon -RX_LOST

# beacon
beacon RX_LOST
#beacon -RX_SET
beacon RX_SET

# led
#led 0 0,0::C:0
led 0 0,0::L:0
#led 1 0,0::C:0
led 1 1,0::L:0
#led 2 0,0::C:0
led 2 2,0::L:0

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
set acc_calibration = 63,18,19,1
#set baro_hardware = AUTO
set baro_hardware = NONE
#set min_check = 1050
set min_check = 1000
#set max_check = 1900
set max_check = 2000
#set rssi_channel = 0
set rssi_channel = 5
#set dshot_bidir = ON
set dshot_bidir = OFF
#set motor_pwm_protocol = DSHOT600
set motor_pwm_protocol = DSHOT300
#set align_board_yaw = 0
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
set vtx_power = 1
#set vtx_freq = 0
set vtx_freq = 5705
#set vcd_video_system = HD
set vcd_video_system = NTSC
#set gyro_1_sensor_align = CW0
set gyro_1_sensor_align = DEFAULT
#set gyro_1_align_yaw = 0
set gyro_1_align_yaw = 1800
#set craft_name = -
set craft_name = Protek 35

profile 0

# profile 0
#set iterm_relax = RP
set iterm_relax = RPY
#set iterm_relax_cutoff = 15
set iterm_relax_cutoff = 10
#set yaw_lowpass_hz = 100
set yaw_lowpass_hz = 80
#set throttle_boost = 5
set throttle_boost = 0
#set p_pitch = 47
set p_pitch = 65
#set i_pitch = 84
set i_pitch = 99
#set d_pitch = 46
set d_pitch = 48
#set f_pitch = 125
set f_pitch = 116
#set p_roll = 45
set p_roll = 58
#set i_roll = 80
set i_roll = 94
#set d_roll = 40
set d_roll = 46
#set f_roll = 120
set f_roll = 109
#set p_yaw = 45
set p_yaw = 50
#set i_yaw = 80
set i_yaw = 99
#set f_yaw = 120
set f_yaw = 109
#set d_min_pitch = 34
set d_min_pitch = 31
#set feedforward_transition = 0
set feedforward_transition = 40
#set tpa_rate = 65
set tpa_rate = 50
#set tpa_breakpoint = 1350
set tpa_breakpoint = 1200

profile 1

profile 2

profile 3

# restore original profile selection
profile 0

rateprofile 0

# rateprofile 0
#set thr_mid = 50
set thr_mid = 100
#set thr_expo = 0
set thr_expo = 20
#set roll_rc_rate = 7
set roll_rc_rate = 19
#set pitch_rc_rate = 7
set pitch_rc_rate = 19
#set yaw_rc_rate = 7
set yaw_rc_rate = 19
#set roll_expo = 0
set roll_expo = 60
#set pitch_expo = 0
set pitch_expo = 60
#set yaw_expo = 0
set yaw_expo = 60
#set roll_srate = 67
set roll_srate = 90
#set pitch_srate = 67
set pitch_srate = 90
#set yaw_srate = 67
set yaw_srate = 90

rateprofile 1

rateprofile 2

rateprofile 3

# restore original rateprofile selection
rateprofile 0

# save configuration
save
# 