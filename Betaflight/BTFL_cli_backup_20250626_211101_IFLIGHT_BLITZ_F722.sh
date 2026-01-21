diff all defaults

# version
# Betaflight / STM32F7X2 (S7X2) 4.5.2 Mar 20 2025 / 03:51:23 (024f8e13d) MSP API: 1.46
# config rev: 0f78778

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name IFLIGHT_BLITZ_F722
manufacturer_id IFRC
mcu_id 001c002b3331510f33323639
signature 

# name: Chimera 7 Pro
#feature -GPS
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD

# feature
feature GPS
feature TELEMETRY
feature LED_STRIP
feature OSD

#beacon -RX_LOST

# beacon
beacon RX_LOST
#beacon -RX_SET
beacon RX_SET

# serial
#serial 0 0 115200 57600 0 115200
serial 0 1 115200 57600 0 115200
#serial 1 0 115200 57600 0 115200
serial 1 64 115200 57600 0 115200
#serial 3 0 115200 57600 0 115200
serial 3 2 115200 115200 0 115200

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

# master
#set dyn_notch_q = 300
set dyn_notch_q = 250
#set dyn_notch_max_hz = 600
set dyn_notch_max_hz = 400
#set acc_trim_pitch = 0
set acc_trim_pitch = -4
#set acc_trim_roll = 0
set acc_trim_roll = 2
#set acc_calibration = 0,0,0,0
set acc_calibration = 28,26,7,1
#set dshot_bidir = OFF
set dshot_bidir = ON
#set vbat_max_cell_voltage = 430
set vbat_max_cell_voltage = 422
#set yaw_motors_reversed = OFF
set yaw_motors_reversed = ON
#set small_angle = 25
set small_angle = 180
#set gps_sbas_mode = NONE
set gps_sbas_mode = AUTO
#set osd_vbat_pos = 341
set osd_vbat_pos = 2433
#set osd_rssi_pos = 341
set osd_rssi_pos = 342
#set osd_link_quality_pos = 341
set osd_link_quality_pos = 2113
#set osd_rssi_dbm_pos = 341
set osd_rssi_dbm_pos = 299
#set osd_tim_1_pos = 341
set osd_tim_1_pos = 295
#set osd_tim_2_pos = 341
set osd_tim_2_pos = 2455
#set osd_flymode_pos = 341
set osd_flymode_pos = 2105
#set osd_throttle_pos = 341
set osd_throttle_pos = 409
#set osd_vtx_channel_pos = 341
set osd_vtx_channel_pos = 2081
#set osd_current_pos = 341
set osd_current_pos = 352
#set osd_mah_drawn_pos = 341
set osd_mah_drawn_pos = 14720
#set osd_craft_name_pos = 341
set osd_craft_name_pos = 2443
#set osd_gps_speed_pos = 341
set osd_gps_speed_pos = 2458
#set osd_gps_lon_pos = 341
set osd_gps_lon_pos = 256
#set osd_gps_lat_pos = 341
set osd_gps_lat_pos = 288
#set osd_gps_sats_pos = 341
set osd_gps_sats_pos = 2426
#set osd_home_dir_pos = 341
set osd_home_dir_pos = 2415
#set osd_home_dist_pos = 341
set osd_home_dist_pos = 2446
#set osd_flight_dist_pos = 341
set osd_flight_dist_pos = 213
#set osd_altitude_pos = 341
set osd_altitude_pos = 2455
#set osd_pidrate_profile_pos = 341
set osd_pidrate_profile_pos = 407
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
#set gyro_1_sensor_align = CW0
set gyro_1_sensor_align = DEFAULT
#set craft_name = -
set craft_name = Chimera 7 Pro

profile 0

# profile 0
#set iterm_relax_cutoff = 15
set iterm_relax_cutoff = 10
#set pidsum_limit = 500
set pidsum_limit = 1000
#set p_pitch = 47
set p_pitch = 100
#set i_pitch = 84
set i_pitch = 81
#set d_pitch = 46
set d_pitch = 70
#set f_pitch = 125
set f_pitch = 120
#set p_roll = 45
set p_roll = 98
#set i_roll = 80
set i_roll = 77
#set d_roll = 40
set d_roll = 64
#set f_roll = 120
set f_roll = 113
#set p_yaw = 45
set p_yaw = 81
#set i_yaw = 80
set i_yaw = 81
#set f_yaw = 120
set f_yaw = 113
#set d_min_roll = 30
set d_min_roll = 0
#set d_min_pitch = 34
set d_min_pitch = 0
#set thrust_linear = 0
set thrust_linear = 25
#set feedforward_transition = 0
set feedforward_transition = 40


profile 1

profile 2

profile 3

# restore original profile selection
profile 0

rateprofile 0

# rateprofile 0
#set roll_rc_rate = 7
set roll_rc_rate = 20
#set pitch_rc_rate = 7
set pitch_rc_rate = 20
#set yaw_rc_rate = 7
set yaw_rc_rate = 20
#set roll_expo = 0
set roll_expo = 54
#set pitch_expo = 0
set pitch_expo = 54
#set yaw_expo = 0
set yaw_expo = 54
#set tpa_rate = 65
set tpa_rate = 55
#set tpa_breakpoint = 1350
set tpa_breakpoint = 1400

rateprofile 1

rateprofile 2

rateprofile 3

rateprofile 4

rateprofile 5

# restore original rateprofile selection
rateprofile 0

# save configuration
save