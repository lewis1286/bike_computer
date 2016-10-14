#!/usr/bin/env python
# coding=utf-8

import pygame
import time
import os
import subprocess
from displays import metrics


# Globals
MARGIN = 15
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 60
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
FONT_SIZE = 45

button_1_dims = [MARGIN, MARGIN, BUTTON_HEIGHT, BUTTON_WIDTH]
button_2_dims = [MARGIN, 2 * MARGIN + BUTTON_HEIGHT,
                 BUTTON_HEIGHT, BUTTON_WIDTH]
button_3_dims = [MARGIN, 3 * MARGIN + 2 * BUTTON_WIDTH,
                 BUTTON_HEIGHT, BUTTON_WIDTH]

# if subprocess.check_output("whoami", shell=True).rstrip() == 'pi':
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDEV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

font1 = pygame.font.SysFont(None, FONT_SIZE)
font2 = pygame.font.SysFont(None, FONT_SIZE - 10)
font3 = pygame.font.SysFont(None, FONT_SIZE + 30)


# initialize display window
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('bike_ui')

# Colors (from hex code AF1224 colorscheme)
white = (218, 242, 239)
black = (43, 43, 43)
red = (175, 18, 36)
teal = (63, 127, 120)


def message_to_screen(msg, color, item):
    if item == "button_1":
        screen_text = pygame.transform.rotozoom(font1.render(msg, True, color), 270, 1)
        location = [40, 40]
    elif item == "speed":
        screen_text = pygame.transform.rotozoom(font2.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN, MARGIN]
    elif item == "speed_val":
        screen_text = pygame.transform.rotozoom(font3.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 3 * MARGIN - BUTTON_HEIGHT, MARGIN]
    elif item == "cadence":
        screen_text = pygame.transform.rotozoom(font2.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - BUTTON_HEIGHT, MARGIN]
    elif item == "cadence_val":
        screen_text = pygame.transform.rotozoom(font3.render(msg, True, color), 270, 1)
        location = [SCREEN_WIDTH - 5 * MARGIN - 2 * BUTTON_HEIGHT, MARGIN]
    gameDisplay.blit(screen_text, location)

gameExit = False
bike_metrics = metrics()

count = 0
while not gameExit:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        # print event
        if event.type == pygame.QUIT:
            pass
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            gameDisplay.fill(red)
            # bike_metrics.make_screen()
    # #wipe slate clean

    # do rendering of new graphics

    # put speed and cadence to screen
    message_to_screen('Current Speed', teal, 'speed')
    message_to_screen('XX.XXX', teal, 'speed_val')
    message_to_screen('Current Cadence', teal, 'cadence')
    message_to_screen('XX.XXX', teal, 'cadence_val')

    pygame.display.update()
    time.sleep(0.1)
    count += 1
    if count == 100:
        gameExit = True

pygame.quit()
# quit

