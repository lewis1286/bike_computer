# holds classes for the different types of displays to show to the screen

import pygame
from pygame.locals import *

class metrics:
    pygame.init()
    # Globals
    MARGIN = 15
    BUTTON_WIDTH = 60
    BUTTON_HEIGHT = 60
    SCREEN_WIDTH = 320
    SCREEN_HEIGHT = 240
    FONT_SIZE = 45

    font1 = pygame.font.SysFont(None, FONT_SIZE)
    font2 = pygame.font.SysFont(None, FONT_SIZE - 10)
    font3 = pygame.font.SysFont(None, FONT_SIZE + 30)

    # Colors (from hex code AF1224 colorscheme)
    white = (218, 242, 239)
    black = (43, 43, 43)
    red = (175, 18, 36)
    teal = (63, 127, 120)

    gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    def message_to_screen(self, msg, color, item):
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


    def print_messages(self):
        # put speed and cadence to screen
        self.message_to_screen('Current Speed', teal, 'speed')
        self.message_to_screen('XX.XXX', teal, 'speed_val')
        self.message_to_screen('Current Cadence', teal, 'cadence')
        self.message_to_screen('XX.XXX', teal, 'cadence_val')

    def make_screen(self):
        gameDisplay.fill(white)
        self.print_messages()

