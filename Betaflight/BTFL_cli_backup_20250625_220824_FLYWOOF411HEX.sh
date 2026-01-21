diff all defaults

# version
# Betaflight / STM32F411 (S411) 4.5.2 Mar 21 2025 / 16:37:18 (024f8e13d) MSP API: 1.46
# config rev: 3eedb40

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name FLYWOOF411HEX
manufacturer_id FLWO
mcu_id 0043001d3030511837393838
signature 

# name: FLYWOO

resource
resource BEEPER 1 C14
resource MOTOR 1 A08
resource MOTOR 2 B03
resource MOTOR 3 B10
resource MOTOR 4 A15
resource MOTOR 5 B06
resource MOTOR 6 B07
resource LED_STRIP 1 A00
resource SERIAL_TX 1 A09
resource SERIAL_TX 2 A02
resource SERIAL_RX 1 A10
resource SERIAL_RX 2 A03
resource SOFTSERIAL_TX 1 B04
resource SOFTSERIAL_RX 1 B00
resource I2C_SCL 1 B08
resource I2C_SDA 1 B09
resource LED 1 C13
resource SPI_SCK 1 A05
resource SPI_SCK 2 B13
resource SPI_SDI 1 A06
resource SPI_SDI 2 B14
resource SPI_SDO 1 A07
resource SPI_SDO 2 B15
resource ADC_BATT 1 B01
resource ADC_CURR 1 A01
resource OSD_CS 1 B12
resource GYRO_EXTI 1 B05
resource GYRO_CS 1 A04
resource USB_DETECT 1 C15

# timer
timer A02 AF3
# pin A02: TIM9 CH1 (AF3)
timer A08 AF1
# pin A08: TIM1 CH1 (AF1)
timer B03 AF1
# pin B03: TIM2 CH2 (AF1)
timer B10 AF1
# pin B10: TIM2 CH3 (AF1)
timer A15 AF1
# pin A15: TIM2 CH1 (AF1)
timer B06 AF2
# pin B06: TIM4 CH1 (AF2)
timer B07 AF2
# pin B07: TIM4 CH2 (AF2)
timer B00 AF2
# pin B00: TIM3 CH3 (AF2)
timer B04 AF2
# pin B04: TIM3 CH1 (AF2)
timer A00 AF2
# pin A00: TIM5 CH1 (AF2)

# dma
#dma ADC 1 1
dma ADC 1 0
# ADC 1: DMA2 Stream 0 Channel 0
dma pin A08 1
# pin A08: DMA2 Stream 1 Channel 6
dma pin B03 0
# pin B03: DMA1 Stream 6 Channel 3
dma pin B10 0
# pin B10: DMA1 Stream 1 Channel 3
dma pin A15 0
# pin A15: DMA1 Stream 5 Channel 3
dma pin B06 0
# pin B06: DMA1 Stream 0 Channel 2
dma pin B07 0
# pin B07: DMA1 Stream 3 Channel 2
dma pin B00 0
# pin B00: DMA1 Stream 7 Channel 5
dma pin B04 0
# pin B04: DMA1 Stream 4 Channel 5
dma pin A00 0
# pin A00: DMA1 Stream 2 Channel 6

# mixer
#mixer QUADX
mixer HEX6X
#mmix 0  0.000  0.000  0.000  0.000
mmix 0  1.000 -0.500  0.866  1.000
#mmix 1  0.000  0.000  0.000  0.000
mmix 1  1.000 -0.500 -0.866  1.000
#mmix 2  0.000  0.000  0.000  0.000
mmix 2  1.000  0.500  0.866 -1.000
#mmix 3  0.000  0.000  0.000  0.000
mmix 3  1.000  0.500 -0.866 -1.000
#mmix 4  0.000  0.000  0.000  0.000
mmix 4  1.000 -1.000  0.000 -1.000
#mmix 5  0.000  0.000  0.000  0.000
mmix 5  1.000  1.000  0.000  1.000
#feature -MOTOR_STOP
#feature -SOFTSERIAL
#feature -GPS
#feature -TELEMETRY

# feature
#feature -LED_STRIP
#feature -OSD
feature MOTOR_STOP
feature SOFTSERIAL
feature GPS
feature TELEMETRY
feature LED_STRIP
feature OSD

# serial
#serial 0 0 115200 57600 0 115200
serial 0 64 115200 57600 0 115200
#serial 1 0 115200 57600 0 115200
serial 1 2 115200 9600 0 115200
#serial 30 0 115200 57600 0 115200
serial 30 8192 115200 19200 0 19200

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
aux 0 0 1 1300 2100 0 0
#aux 1 0 0 900 900 0 0
aux 1 2 1 1700 2100 0 0
#aux 2 0 0 900 900 0 0
aux 2 46 2 1700 2100 0 0
#aux 3 0 0 900 900 0 0
aux 3 13 3 1700 2100 0 0
#aux 4 0 0 900 900 0 0
aux 4 15 3 900 1325 0 0
#aux 5 0 0 900 900 0 0
aux 5 35 0 1700 2100 0 0

# vtxtable
#vtxtable bands 0
vtxtable bands 5
#vtxtable channels 0
vtxtable channels 8
#vtxtable band 1 BAND1    1 CUSTOM 
vtxtable band 1 BAND_A   A CUSTOM  5865 5845 5825 5805 5785 5765 5745 5725
#vtxtable band 2 BAND2    2 CUSTOM 
vtxtable band 2 BAND_B   B CUSTOM  5733 5752 5771 5790 5999 5828 5847 5866
#vtxtable band 3 BAND3    3 CUSTOM 
vtxtable band 3 BAND_E   E CUSTOM  5705 5685 5665 5645 5885 5905 5925 5945
#vtxtable band 4 BAND4    4 CUSTOM 
vtxtable band 4 AIRWAVE  F CUSTOM  5740 5760 5780 5800 5820 5840 5860 5880
#vtxtable band 5 BAND5    5 CUSTOM 
vtxtable band 5 RACEBAND R CUSTOM  5658 5695 5732 5769 5806 5843 5880 5917
#vtxtable powerlevels 0
vtxtable powerlevels 5
#vtxtable powervalues 0 0 0 0 0 0 0 0
vtxtable powervalues 25 100 200 400 600
#vtxtable powerlabels LV0 LV1 LV2 LV3 LV4 LV5 LV6 LV7
vtxtable powerlabels 25 50 100 200 MAX

# master
#set acc_calibration = 0,0,0,0
set acc_calibration = 25,17,0,1
#set rssi_channel = 0
set rssi_channel = 12
#set serialrx_provider = CRSF
set serialrx_provider = SBUS
#set failsafe_procedure = DROP
set failsafe_procedure = GPS-RESCUE
#set current_meter = ADC
set current_meter = NONE
#set small_angle = 25
set small_angle = 180
#set gps_rescue_min_sats = 8
set gps_rescue_min_sats = 5
#set gps_rescue_allow_arming_without_fix = OFF
set gps_rescue_allow_arming_without_fix = ON
#set pid_process_denom = 1
set pid_process_denom = 4
#set osd_vbat_pos = 341
set osd_vbat_pos = 2304
#set osd_rssi_pos = 341
set osd_rssi_pos = 2208
#set osd_rssi_dbm_pos = 341
set osd_rssi_dbm_pos = 128
#set osd_tim_1_pos = 341
set osd_tim_1_pos = 2400
#set osd_tim_2_pos = 341
set osd_tim_2_pos = 2368
#set osd_flymode_pos = 341
set osd_flymode_pos = 2272
#set osd_vtx_channel_pos = 341
set osd_vtx_channel_pos = 2325
#set osd_craft_name_pos = 341
set osd_craft_name_pos = 2048
#set osd_gps_speed_pos = 341
set osd_gps_speed_pos = 2233
#set osd_gps_lon_pos = 341
set osd_gps_lon_pos = 2097
#set osd_gps_lat_pos = 341
set osd_gps_lat_pos = 2065
#set osd_gps_sats_pos = 341
set osd_gps_sats_pos = 2298
#set osd_home_dir_pos = 341
set osd_home_dir_pos = 2265
#set osd_home_dist_pos = 341
set osd_home_dist_pos = 2265
#set osd_flight_dist_pos = 341
set osd_flight_dist_pos = 2201
#set osd_altitude_pos = 341
set osd_altitude_pos = 2135
#set osd_warnings_pos = 14772
set osd_warnings_pos = 14729
#set osd_avg_cell_voltage_pos = 341
set osd_avg_cell_voltage_pos = 2336
#set osd_disarmed_pos = 341
set osd_disarmed_pos = 2411
#set osd_flip_arrow_pos = 341
set osd_flip_arrow_pos = 2112
#set osd_core_temp_pos = 341
set osd_core_temp_pos = 2169
#set vtx_band = 0
set vtx_band = 2
#set vtx_channel = 0
set vtx_channel = 4
#set vtx_power = 0
set vtx_power = 3
#set vtx_freq = 0
set vtx_freq = 5790
#set pinio_box = 255,255,255,255
set pinio_box = 40,41,255,255
#set gyro_2_spibus = 0
set gyro_2_spibus = 1
#set craft_name = -
set craft_name = FLYWOO

profile 0

# profile 0
#set anti_gravity_gain = 80
set anti_gravity_gain = 200
#set iterm_relax_cutoff = 15
set iterm_relax_cutoff = 20
#set p_pitch = 47
set p_pitch = 52
#set i_pitch = 84
set i_pitch = 63
#set d_pitch = 46
set d_pitch = 68
#set f_pitch = 125
set f_pitch = 80
#set p_roll = 45
set p_roll = 47
#set i_roll = 80
set i_roll = 59
#set d_roll = 40
set d_roll = 63
#set f_roll = 120
set f_roll = 76
#set p_yaw = 45
set p_yaw = 50
#set i_yaw = 80
set i_yaw = 63
#set f_yaw = 120
set f_yaw = 76
#set d_min_roll = 30
set d_min_roll = 41
#set d_min_pitch = 34
set d_min_pitch = 45
#set tpa_breakpoint = 1350
set tpa_breakpoint = 1250

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