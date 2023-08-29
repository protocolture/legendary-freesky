#!/usr/bin/python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

Relay = [5, 6, 13, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(0,1):
    GPIO.setup(Relay[0], GPIO.OUT)
    GPIO.output(Relay[0], GPIO.HIGH)

try:
    while True:
        for i in range(8):
            GPIO.output(Relay[0], GPIO.LOW)
            time.sleep(1)
        for i in range(8):
            GPIO.output(Relay[0], GPIO.HIGH)
            time.sleep(10)


except:
    GPIO.cleanup()
