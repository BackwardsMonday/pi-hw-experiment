#! /usr/bin/python

from gpiozero import RGBLED
from time import sleep
import random

led = RGBLED(21, 26, 13)
def rgbConvert(color):
    return (1-color[0]/255,1-color[1]/255,1-color[2]/255)

changes = 1000
colors = {}
colors['green'] = (0,255,0)
colors['red'] = (255, 0, 0)
colors['blue'] = (0, 0, 255)
colors['yellow'] = (255, 255, 0)
colors['purpule'] = (255, 0, 255)
colors['teal'] = (0, 128, 128)
colors['orange'] = (255, 115, 0)
colors['warmWhite'] = (255, 244, 229)


for i in range(changes):
    rColor, rValue = random.choice(list(colors.items()))
    print(rColor)
    led.color = rgbConvert(rValue)
    sleep(0.1)
