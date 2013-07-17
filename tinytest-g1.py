#! /usr/bin/python

import sys
import serial
import time
from time import sleep

serial = serial.Serial("/dev/ttyUSB0", baudrate=115200, xonxoff=False, timeout=0.5)

serial.write("\n")
serial.write("?\n")
response = serial.readlines(None)
print str(response)
sleep(1)

# set origin offset
serial.write("g92 x0 y0 \r\n")
print "g92 x0 y0 \r\n"
sleep(1)
print serial.readlines(None)
sleep(1)

# drive motors to 0, 0
serial.write("g0 x0 y0\n")
print "g0 x0 y0"
print serial.readlines(None)
sleep(1)
serial.write("g1 x0 y0 f10000\n")
print serial.readlines(None)
serial.write("g1 x50 y0 f10000\n")
print serial.readlines(None)
serial.write("g1 x0 y50 f10000\n")
print serial.readlines(None)
serial.write("g1 x100 y100 f10000\n")
print serial.readlines(None)
serial.write("g1 x0 y0 f10000\n")
print serial.readlines(None)
