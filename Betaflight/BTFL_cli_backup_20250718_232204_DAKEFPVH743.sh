# diff all defaults

# version
# Betaflight / STM32H743 (SH74) 4.5.1 Apr 29 2025 / 17:22:03 (14ea0c387) MSP API: 1.46
# config rev: 14ea0c387

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name DAKEFPVH743
manufacturer_id DAKE
mcu_id 0017002e3233510834353936
signature 
#feature -SERVO_TILT
#feature -RANGEFINDER
#feature -TELEMETRY
#feature -LED_STRIP
#feature -DISPLAY
#feature -OSD
#feature -CHANNEL_FORWARDING
#feature -TRANSPONDER

# feature
feature SERVO_TILT
feature RANGEFINDER
feature TELEMETRY
feature LED_STRIP
feature DISPLAY
feature OSD
feature CHANNEL_FORWARDING
feature TRANSPONDER

# master
#set acc_calibration = 0,0,0,0
set acc_calibration = -29,-13,0,1
#set osd_canvas_height = 16
set osd_canvas_height = 13

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