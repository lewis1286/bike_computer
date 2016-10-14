#!/usr/bin/env python
# coding=utf-8

import pygame
import time
import os
import subprocess
import RPi.GPIO as GPIO
import time
import datetime
from objects import *

###########################   GPIO setup ###############################
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)
# print "Setup GPIO pin as input"
# Set Switch GPIO as input
GPIO.setup(17 , GPIO.IN)
GPIO.setup(22 , GPIO.IN)
##############################################################


######################### Globals ##############################################
MARGIN = 15
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 60
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
FONT_SIZE = 45
##############################################################

# button_1_dims = [MARGIN, MARGIN, BUTTON_HEIGHT, BUTTON_WIDTH]
# button_2_dims = [MARGIN, 2 * MARGIN + BUTTON_HEIGHT,
                 # BUTTON_HEIGHT, BUTTON_WIDTH]
# button_3_dims = [MARGIN, 3 * MARGIN + 2 * BUTTON_WIDTH,
                 # BUTTON_HEIGHT, BUTTON_WIDTH]

# if subprocess.check_output("whoami", shell=True).rstrip() == 'pi':

###########################  pygame initializations ############################
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDEV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('bike_ui')
gameExit = False
################################################################################


###########################   colores and fonts ############################
# Colors (from hex code AF1224 colorscheme)
white = (218, 242, 239)
black = (43, 43, 43)
red = (175, 18, 36)
teal = (63, 127, 120)

font1 = pygame.font.SysFont(None, FONT_SIZE)
font2 = pygame.font.SysFont(None, FONT_SIZE - 10)
font3 = pygame.font.SysFont(None, FONT_SIZE + 30)
font_tiny = pygame.font.SysFont(None, FONT_SIZE - 30)
font_small = pygame.font.SysFont(None, FONT_SIZE - 15)

################################################################################

cadence = Cadence()
wheel = Wheel()

def sensorCallback1(channel):
  # Called if sensor output goes LOW
    # timestamp = time.time()
    # stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    # print "Sensor LOW, magnet 17 detected " + stamp
    wheel.increment()
    # if wheel.total_ticks() > 5:
        # print 'woohoo! ' + str(wheel.speed())
        # print 'total_ticks: ' + str(wheel.total_ticks())
        # print 'total_time: ' + str(wheel.total_time())


def sensorCallback2(channel):
    # Called if sensor output goes HIGH
    # timestamp = time.time()
    # stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    cadence.increment()
    # print "Sensor LOW, magnet 22 detected " + stamp


GPIO.add_event_detect(17, GPIO.FALLING, callback=sensorCallback1)
GPIO.add_event_detect(22, GPIO.FALLING, callback=sensorCallback2)


def message_to_screen(msg, color, item):
    if item == "speed":
        screen_text = pygame.transform.rotozoom(font2.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN, MARGIN]
    elif item == "speed_val":
        screen_text = pygame.transform.rotozoom(font3.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN - BUTTON_HEIGHT, MARGIN]
    elif item == "distance":
        screen_text = pygame.transform.rotozoom(font2.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - BUTTON_HEIGHT, MARGIN]
    elif item == "distance_val":
        screen_text = pygame.transform.rotozoom(font3.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - 2 * BUTTON_HEIGHT, MARGIN]
    elif item == "cadence":
        screen_text = pygame.transform.rotozoom(font_small.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - 3.2 * BUTTON_HEIGHT, 8 * MARGIN]
    elif item == "cadence_val":
        screen_text = pygame.transform.rotozoom(font3.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - 4 * BUTTON_HEIGHT, 10 * MARGIN]
    elif item == "time":
        screen_text = pygame.transform.rotozoom(font_small.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN - 3 * BUTTON_HEIGHT, MARGIN]
    elif item == "time_val":
        screen_text = pygame.transform.rotozoom(font_small.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN - 3 * BUTTON_HEIGHT, 7 * MARGIN]

    gameDisplay.blit(screen_text, location)



background = white
count = 0
while not gameExit:
    gameDisplay.fill(background)
    for event in pygame.event.get():
        # print event
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if background == white:
                background = red
            else:
                background = white
            gameDisplay.fill(background)
    # #wipe slate clean

    # do rendering of new graphics

    # put speed and distance to screen
    message_to_screen('Current Speed mph', teal, 'speed')
    message_to_screen(str(round(wheel.speed(), 2)), teal, 'speed_val')
    message_to_screen('Total distance mi', teal, 'distance')
    message_to_screen(str(round(wheel.total_distance(), 4)), teal, 'distance_val')
    message_to_screen('Cadence', teal, 'cadence')
    message_to_screen(str(int(cadence.cadence())), teal, 'cadence_val')
    message_to_screen('Time', teal, 'time')
    message_to_screen(wheel.total_time(), teal, 'time_val')


    pygame.display.update()
    time.sleep(0.1)
    count += 1
    if count == 300:
        gameExit = True
        # reset GPIO settings
        GPIO.cleanup()

pygame.quit()

