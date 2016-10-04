#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the hall effect sensors on GPIO17 and GPIO18.
#
# Author : Lewis Guignard
# Date   : 27/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print "Setup GPIO pin as input"

# Set Switch GPIO as input
GPIO.setup(17 , GPIO.IN)
GPIO.setup(18 , GPIO.IN)

def sensorCallback1(channel):
  # Called if sensor output goes LOW
    timestamp = time.time()
    stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  # print "Sensor LOW, magnet 17 detected " + stamp
    add speed_tick()


def sensorCallback2(channel):
  # Called if sensor output goes HIGH
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print "Sensor LOW, magnet 18 detected " + stamp

def get speed():
    return 0

def main():
    # Wrap main content in a try block so we can
    # catch the user pressing CTRL-C and run the
    # GPIO cleanup function. This will also prevent
    # the user seeing lots of unnecessary error
    # messages.

    GPIO.add_event_detect(17, GPIO.FALLING, callback=sensorCallback1)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=sensorCallback2)

    try:
    # Loop until users quits with CTRL-C
    while True :
        time.sleep(0.1)

    except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

if __name__=="__main__":
    main()
