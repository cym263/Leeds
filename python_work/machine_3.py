#!/usr/bin/python2.7
 
import serial
 
from datetime import datetime
ser = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE)


while ser.isOpen():
 datastring = ser.read(size=8)
 print datetime.utcnow().isoformat(), datastring
#print datetime.utcnow().isoformat(), ser.read(size=8)

#print datetime.utcnow().isoformat(), ser.read(size=8)
ser.close() 