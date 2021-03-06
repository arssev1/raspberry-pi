#!/usr/bin/python
# Python script by arssev1
# Need RPi.GPIO lib
# Gets voltage from MCP3201 analog pin

import RPi.GPIO as GPIO

CS = 8
DOUT = 9
CLK = 11

vc = 3.3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(CLK, GPIO.OUT)

binData = 0;

GPIO.output(CS, True)
GPIO.output(CLK, True)
GPIO.output(CS, False)

i1 = 14

while (i1 >= 0):
    GPIO.output(CLK, False)
    bitDOUT = GPIO.input(DOUT)
    GPIO.output(CLK, True)
    bitDOUT = bitDOUT << i1
    binData |= bitDOUT
    i1 -= 1

GPIO.output(CS, True)
binData &= 0xFFF
res = round(vc * binData/4096.0, 2)
print('Voltage=' + str(res) + 'V')
