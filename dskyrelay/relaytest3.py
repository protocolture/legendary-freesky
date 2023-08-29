#!/usr/bin/python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

Relay = [5, 6, 13, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Relay[0], GPIO.OUT)
GPIO.output(Relay[0], GPIO.HIGH)

try:
        for i in range(8):
            GPIO.output(Relay[0], GPIO.LOW)
            GPIO.output(Relay[0], GPIO.HIGH)
            time.sleep(10)
            GPIO.output(Relay[0], GPIO.LOW)
            
