import serial
from time import sleep
ser = serial.Serial('/dev/ttyUSB1', 115200)

sleep(1) # give time for reset. This method is from my own library

mesg = 'Beagle\n'
while True:
  ser.write(chr(13).encode('ascii')) # establishes serial connection 
  sleep(1) # give time for reset. This method is from my own library
  ser.write(mesg.encode('ascii'))


