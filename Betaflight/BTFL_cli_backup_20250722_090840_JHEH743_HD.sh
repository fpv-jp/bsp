# diff all defaults
###WARNING: NO CUSTOM DEFAULTS FOUND###

# version
# Betaflight / STM32H743 (SH74) 4.4.3 Nov 30 2023 / 07:36:06 (738127e7e) MSP API: 1.45
###ERROR IN diff: NO CONFIG FOUND###
# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name JHEH743_HD
manufacturer_id JHEF
mcu_id 003000233430511435353737
signature 

# resources
#resource BEEPER 1 NONE
resource BEEPER 1 E03
#resource MOTOR 1 NONE
resource MOTOR 1 A00
#resource MOTOR 2 NONE
resource MOTOR 2 A01
#resource MOTOR 3 NONE
resource MOTOR 3 A02
#resource MOTOR 4 NONE
resource MOTOR 4 A03
#resource MOTOR 5 NONE
resource MOTOR 5 B00
#resource MOTOR 6 NONE
resource MOTOR 6 B01
#resource MOTOR 7 NONE
resource MOTOR 7 C08
#resource MOTOR 8 NONE
resource MOTOR 8 C09
#resource LED_STRIP 1 NONE
resource LED_STRIP 1 A08
#resource SERIAL_TX 1 NONE
resource SERIAL_TX 1 A09
#resource SERIAL_TX 2 NONE
resource SERIAL_TX 2 D05
#resource SERIAL_TX 3 NONE
resource SERIAL_TX 3 D08
#resource SERIAL_TX 4 NONE
resource SERIAL_TX 4 D01
#resource SERIAL_TX 5 NONE
resource SERIAL_TX 5 C12
#resource SERIAL_TX 6 NONE
resource SERIAL_TX 6 C06
#resource SERIAL_TX 7 NONE
resource SERIAL_TX 7 E08
#resource SERIAL_TX 8 NONE
resource SERIAL_TX 8 E01
#resource SERIAL_RX 1 NONE
resource SERIAL_RX 1 A10
#resource SERIAL_RX 2 NONE
resource SERIAL_RX 2 D06
#resource SERIAL_RX 3 NONE
resource SERIAL_RX 3 D09
#resource SERIAL_RX 4 NONE
resource SERIAL_RX 4 D00
#resource SERIAL_RX 5 NONE
resource SERIAL_RX 5 D02
#resource SERIAL_RX 6 NONE
resource SERIAL_RX 6 C07
#resource SERIAL_RX 7 NONE
resource SERIAL_RX 7 E07
#resource SERIAL_RX 8 NONE
resource SERIAL_RX 8 E00
#resource I2C_SCL 1 NONE
resource I2C_SCL 1 B06
#resource I2C_SCL 2 NONE
resource I2C_SCL 2 B10
#resource I2C_SDA 1 NONE
resource I2C_SDA 1 B07
#resource I2C_SDA 2 NONE
resource I2C_SDA 2 B11
#resource LED 1 NONE
resource LED 1 E05
#resource LED 2 NONE
resource LED 2 E04
#resource SPI_SCK 1 NONE
resource SPI_SCK 1 A05
#resource SPI_SCK 2 NONE
resource SPI_SCK 2 B13
#resource SPI_SCK 3 NONE
resource SPI_SCK 3 C10
#resource SPI_SCK 4 NONE
resource SPI_SCK 4 E12
#resource SPI_MISO 1 NONE
resource SPI_MISO 1 A06
#resource SPI_MISO 2 NONE
resource SPI_MISO 2 B14
#resource SPI_MISO 3 NONE
resource SPI_MISO 3 C11
#resource SPI_MISO 4 NONE
resource SPI_MISO 4 E13
#resource SPI_MOSI 1 NONE
resource SPI_MOSI 1 A07
#resource SPI_MOSI 2 NONE
resource SPI_MOSI 2 B15
#resource SPI_MOSI 3 NONE
resource SPI_MOSI 3 B02
#resource SPI_MOSI 4 NONE
resource SPI_MOSI 4 E14
#resource ADC_BATT 1 NONE
resource ADC_BATT 1 C01
#resource ADC_CURR 1 NONE
resource ADC_CURR 1 C03
#resource ADC_EXT 1 NONE
resource ADC_EXT 1 C00
#resource PINIO 1 NONE
resource PINIO 1 C02
#resource PINIO 2 NONE
resource PINIO 2 C05
#resource FLASH_CS 1 NONE
resource FLASH_CS 1 A15
#resource OSD_CS 1 NONE
resource OSD_CS 1 B12
#resource GYRO_EXTI 1 NONE
resource GYRO_EXTI 1 C04
#resource GYRO_EXTI 2 NONE
resource GYRO_EXTI 2 E15
#resource GYRO_CS 1 NONE
resource GYRO_CS 1 A04
#resource GYRO_CS 2 NONE
resource GYRO_CS 2 E11
#resource USB_DETECT 1 NONE
resource USB_DETECT 1 E06

# timer
timer A00 AF2
# pin A00: TIM5 CH1 (AF2)
timer A01 AF2
# pin A01: TIM5 CH2 (AF2)
timer A02 AF2
# pin A02: TIM5 CH3 (AF2)
timer A03 AF2
# pin A03: TIM5 CH4 (AF2)
timer B00 AF2
# pin B00: TIM3 CH3 (AF2)
timer B01 AF2
# pin B01: TIM3 CH4 (AF2)
timer C08 AF3
# pin C08: TIM8 CH3 (AF3)
timer C09 AF3
# pin C09: TIM8 CH4 (AF3)
timer A08 AF1
# pin A08: TIM1 CH1 (AF1)
timer B08 AF1
# pin B08: TIM16 CH1 (AF1)
timer B09 AF1
# pin B09: TIM17 CH1 (AF1)

# dma
#dma ADC 1 NONE
dma ADC 1 8
# ADC 1: DMA2 Stream 0 Request 9
#dma ADC 3 NONE
dma ADC 3 9
# ADC 3: DMA2 Stream 1 Request 115
#dma TIMUP 1 NONE
dma TIMUP 1 0
# TIMUP 1: DMA1 Stream 0 Request 15
#dma TIMUP 3 NONE
dma TIMUP 3 2
# TIMUP 3: DMA1 Stream 2 Request 27
#dma TIMUP 5 NONE
dma TIMUP 5 0
# TIMUP 5: DMA1 Stream 0 Request 59
#dma TIMUP 8 NONE
dma TIMUP 8 4
# TIMUP 8: DMA1 Stream 4 Request 51
#dma pin A00 NONE
dma pin A00 0
# pin A00: DMA1 Stream 0 Request 55
#dma pin A01 NONE
dma pin A01 1
# pin A01: DMA1 Stream 1 Request 56
#dma pin A02 NONE
dma pin A02 2
# pin A02: DMA1 Stream 2 Request 57
#dma pin A03 NONE
dma pin A03 3
# pin A03: DMA1 Stream 3 Request 58
#dma pin B00 NONE
dma pin B00 4
# pin B00: DMA1 Stream 4 Request 25
#dma pin B01 NONE
dma pin B01 5
# pin B01: DMA1 Stream 5 Request 26
#dma pin C08 NONE
dma pin C08 6
# pin C08: DMA1 Stream 6 Request 49
#dma pin C09 NONE
dma pin C09 7
# pin C09: DMA1 Stream 7 Request 50
#dma pin A08 NONE
dma pin A08 14
# pin A08: DMA2 Stream 6 Request 11
#dma pin B08 NONE
dma pin B08 0
# pin B08: DMA1 Stream 0 Request 109
#dma pin B09 NONE
dma pin B09 0
# pin B09: DMA1 Stream 0 Request 111
#feature -TELEMETRY
#feature -LED_STRIP
#feature -OSD

# feature
feature -AIRMODE
feature TELEMETRY
feature LED_STRIP
feature OSD
#feature AIRMODE

# serial
#serial 5 0 115200 57600 0 115200
serial 5 8192 115200 57600 0 115200

# led
#led 0 0,0::C:0
led 0 7,8::CB:8
#led 1 0,0::C:0
led 1 8,8::CB:8
#led 2 0,0::C:0
led 2 9,8::CB:8
#led 3 0,0::C:0
led 3 10,8::CB:8

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
vtxtable band 3 BOSCAM_E E CUSTOM  5705 5685 5665 5645 5885 5905 5925 5945
#vtxtable band 4 BAND4    4 CUSTOM 
vtxtable band 4 FATSHARK F CUSTOM  5740 5760 5780 5800 5820 5840 5860 5880
#vtxtable band 5 BAND5    5 CUSTOM 
vtxtable band 5 RACEBAND R CUSTOM  5658 5695 5732 5769 5806 5843 5880 5917
#vtxtable powerlevels 0
vtxtable powerlevels 5
#vtxtable powervalues 0 0 0 0 0 0 0 0
vtxtable powervalues 25 200 400 800 1600
#vtxtable powerlabels LV0 LV1 LV2 LV3 LV4 LV5 LV6 LV7
vtxtable powerlabels 25 200 400 800 MAX

# master
#set gyro_to_use = FIRST
set gyro_to_use = BOTH
#set acc_calibration = 0,0,0,0
set acc_calibration = -36,-51,3,1
#set mag_bustype = SPI
set mag_bustype = I2C
#set mag_i2c_device = 0
set mag_i2c_device = 1
#set baro_i2c_device = 0
set baro_i2c_device = 1
#set serialrx_provider = SPEK1024
set serialrx_provider = CRSF
#set blackbox_device = SERIAL
set blackbox_device = SPIFLASH
#set motor_pwm_protocol = DISABLED
set motor_pwm_protocol = DSHOT600
#set current_meter = VIRTUAL
set current_meter = ADC
#set battery_meter = NONE
set battery_meter = ADC
#set ibata_scale = 400
set ibata_scale = 170
#set beeper_inversion = OFF
set beeper_inversion = ON
#set beeper_od = ON
set beeper_od = OFF
#set yaw_motors_reversed = OFF
set yaw_motors_reversed = ON
#set osd_vbat_pos = 234
set osd_vbat_pos = 2347
#set osd_crosshairs_pos = 205
set osd_crosshairs_pos = 2253
#set osd_ah_sbar_pos = 206
set osd_ah_sbar_pos = 2254
#set osd_ah_pos = 78
set osd_ah_pos = 2126
#set osd_current_pos = 234
set osd_current_pos = 2442
#set osd_warnings_pos = 14665
set osd_warnings_pos = 14697
#set osd_canvas_width = 53
set osd_canvas_width = 30
#set osd_canvas_height = 20
set osd_canvas_height = 13
#set vtx_band = 0
set vtx_band = 3
#set vtx_channel = 0
set vtx_channel = 6
#set vtx_power = 0
set vtx_power = 1
#set vtx_low_power_disarm = OFF
set vtx_low_power_disarm = ON
#set vtx_freq = 0
set vtx_freq = 5905
#set max7456_spi_bus = 0
set max7456_spi_bus = 2
#set pinio_config = 1,1,1,1
set pinio_config = 129,129,1,1
#set pinio_box = 255,255,255,255
set pinio_box = 0,40,255,255
#set flash_spi_bus = 0
set flash_spi_bus = 3
#set gyro_1_spibus = 0
set gyro_1_spibus = 1
#set gyro_1_sensor_align = CW0
set gyro_1_sensor_align = CW180
#set gyro_1_align_yaw = 0
set gyro_1_align_yaw = 1800
#set gyro_2_spibus = 0
set gyro_2_spibus = 4

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