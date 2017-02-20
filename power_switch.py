#!/usr/bin/env python
# coding=utf-8

# called in /etc/rc.local on boot
# adapted from: http://www.3cc.org/blog/2013/01/raspberry-pi-shutdown-switch-safely-turning-off-the-pi/


import RPi.GPIO as GPIO
import time
import os


# Globals
POWER_PIN = 25  # GPIO pin of power switch
GPIO.setmode(GPIO.BCM)

# using gpio number 18
GPIO.setup(POWER_PIN,
           GPIO.IN,
           pull_up_down=GPIO.PUD_UP)


def Shutdown(channel):
    print 'oh shit'
    os.system("sudo shutdown -h now")


GPIO.add_event_detect(POWER_PIN,
                      GPIO.FALLING,
                      callback=Shutdown,
                      bouncetime=2000)

while 1:
    time.sleep(1)
