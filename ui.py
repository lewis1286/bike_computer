#!/usr/bin/env python
# coding=utf-8

import pygame
import time

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

# pygame.display.update()

gameExit = False

def check_which_button(x, y):
    # check which button was pressed.  returns number of button
    if button_1_dims[0] <= x <= button_1_dims[0] + button_1_dims[2] and \
            button_1_dims[1] <= y <= button_1_dims[1] + button_1_dims[3]:
        # print 'you pressed button 1'
        message_to_screen('1', black, 'button_1')
        pygame.display.update()
        time.sleep(1)
        pygame.draw.rect(gameDisplay, black, button_1_dims)
        return 1
    elif button_2_dims[0] <= x <= button_2_dims[0] + button_2_dims[2] and \
            button_2_dims[1] <= y <= button_2_dims[1] + button_2_dims[3]:
        print 'you pressed button 2'
        gameExit = True
        quit()
        pygame.draw.rect(gameDisplay, black, button_2_dims)
        return 2

    elif button_3_dims[0] <= x <= button_3_dims[0] + button_3_dims[2] and \
            button_3_dims[1] <= y <= button_3_dims[1] + button_3_dims[3]:
        print 'you pressed button 3'
        pygame.draw.rect(gameDisplay, black, button_3_dims)
        return 3
    else:
        return 0

count = 0
while not gameExit:
    for event in pygame.event.get():
        # print event
        if event.type == pygame.QUIT:
            pass
            # gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print 'mouse pressed', event.pos
            pass
            # x, y = event.pos
            # button_pressed = check_which_button(x, y)
    # #wipe slate clean
    gameDisplay.fill(white)

    # do rendering of new graphics
    # [left, top, width, height]
    # button_1 = pygame.draw.rect(gameDisplay, red, button_1_dims)
    # button_2 = pygame.draw.rect(gameDisplay, red, button_2_dims)
    # button_3 = pygame.draw.rect(gameDisplay, red, button_3_dims)

    # # put speed and cadence to screen
    # message_to_screen('Current Speed', teal, 'speed')
    # message_to_screen('XX.XXX', teal, 'speed_val')
    # message_to_screen('Current Cadence', teal, 'cadence')
    # message_to_screen('XX.XXX', teal, 'cadence_val')

    pygame.display.update()
    time.sleep(0.1)
    count += 1
    if count == 100:
        gameExit = True

pygame.quit()
# quit

