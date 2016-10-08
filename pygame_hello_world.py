import pygame
import os
from time import sleep
import random
# import RPi.GPIO as GPIO

#Note #21 changed to #27 for rev2 Pi
button_map = {23:(255,0,0), 22:(0,255,0), 27:(0,0,255), 18:(0,0,0)}

#Setup the GPIOs as inputs with Pull Ups since the buttons are connected to GND
# GPIO.setmode(GPIO.BCM)
# for k in button_map.keys():
    # GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Colors (from hex code AF1224 colorscheme)
white = (218, 242, 239)
black = (43, 43, 43)
red = (175, 18, 36)
teal = (63, 127, 120)

colors = [white, black, red, teal]

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill(teal)
pygame.display.update()

font_big = pygame.font.Font(None, 100)

count = 0
events = []
while True:
    # Scan the buttons
    for event in pygame.event.get():
        # events += str(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            lcd.fill(random.choice(colors))
            pygame.display.update()
    # for (k,v) in button_map.items():
        # print k, v
        # if GPIO.input(k) == False:
            # lcd.fill(v)
            # text_surface = font_big.render('%d'%k, True, WHITE)
            # rect = text_surface.get_rect(center=(160,120))
            # lcd.blit(text_surface, rect)
            # pygame.display.update()
    count += 1
    if count == 100:
        # print events
        quit()
    sleep(0.1)
