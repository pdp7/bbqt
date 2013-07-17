import serial
import time
serial = serial.Serial("/dev/ttyUSB0", baudrate=115200)

while True:
        serial.write('foo\n')
        time.sleep(2)
