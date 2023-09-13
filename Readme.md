# Overview

Need a tool for uploading your firmware using simple steps? 
Do you need a way to do a usb reset signal for uploading as platformio/Arduino IDE: 
`Performing 1200-bps touch reset on serial port COM1`

This is for you

# Requirements

Python
pyserial (pip install pyserial)


# Instructions

1. Reset the board/trigger bootloader (will do it on the first port found)

In a terminal run: 
 python pyTouchAuto.py

- If you want to specify a port, modify the code of pyTouch.py and run
 python pyTouch.py

2. Run upload command, eg. bossac (included in folder)

path/to/bossac -i -d --port=ttyACM0 -U false -e -w  -b "path/to/firmware.bin" -R

Refer to bossac manual for details on the used option/switches (-idUewbR)

Examples:

In a Linux terminal: 
./1.6.1-arduino/bossac -i -d --port=ttyACM0 -U false -e -w  -b "./firmware.bin" -R

In Windows: 
./1.6.1-arduino/bossac -i -d --port=COMn -U false -e -w  -b "firmware.bin" -R

Example for an sketch build in Arduino IDE:

"/home/axel/.arduino15/packages/arduino/tools/bossac/1.6.1-arduino/bossac" -i -d --port=ttyACM0 -U false -e -w  -b "/tmp/arduino/sketches/9AD2B3422801741548BD78F5F71C95A7/Blink_arm.ino.bin" -R



