import pygame
import os
import pygameui as ui
import logging
import RPi.GPIO as GPIO
import time

#Setup the GPIOs as outputs - only 4 and 17 are available
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

MARGIN = 15
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 50
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 320

class PiTft(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        self.button_1 = ui.Button(ui.Rect(MARGIN, SCREEN_HEIGHT - BUTTON_HEIGHT - MARGIN,
                                          BUTTON_WIDTH, BUTTON_HEIGHT), '1')
        self.button_1.on_clicked.connect(self.gpi_button)
        self.add_child(self.button_1)

        self.button_2 = ui.Button(ui.Rect(2 * MARGIN + BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT - MARGIN,
                                          BUTTON_WIDTH, BUTTON_HEIGHT), '2')
        self.button_2.on_clicked.connect(self.gpi_button)
        self.add_child(self.button_2)

        self.button_3 = ui.Button(ui.Rect(3 * MARGIN + 2 * BUTTON_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT - MARGIN,
                                          BUTTON_WIDTH, BUTTON_HEIGHT), '3')
        self.button_3.on_clicked.connect(self.gpi_button)
        self.add_child(self.button_3)

        # self.off4_button = ui.Button(ui.Rect(170, BUTTON_WIDTH, BUTTON_WIDTH, 90), '4 off')
        # self.off4_button.on_clicked.connect(self.gpi_button)
        # self.add_child(self.off4_button)

    def gpi_button(self, btn, mbtn):
        logger.info(btn.text)

        if btn.text == '1':
            quit()
            # GPIO.output(17, False)
        elif btn.text == '2':
            GPIO.output(4, False)
        elif btn.text == '3':
            GPIO.output(17, True)
        # elif btn.text == '4 off':
            # GPIO.output(4, True)

    # time.sleep(9)
    # quit()

# ui.init('Raspberry Pi UI', (320, 240))
ui.init('Raspberry Pi UI', (240, 320))

pygame.mouse.set_visible(False)
ui.scene.push(PiTft())
ui.run()

