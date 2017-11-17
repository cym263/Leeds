#!/usr/bin/python2.7
 
import serial
 
from datetime import datetime
import serial
ser = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600,)

i=0
while i < 9:
  i += 1
  print datetime.utcnow().isoformat(), ser.read(size=8)
ser.close() 
