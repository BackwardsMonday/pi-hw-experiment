#! /usr/bin/python

from gpiozero import RGBLED
from time import sleep
import random

led = RGBLED(21, 26, 13)

changes = 10
fadeIn = 10
fadeOut = 5
onTime = 5
offTime = 5

colors = {}
colors['green'] = (0,255,0)
colors['red'] = (255, 0, 0)
colors['blue'] = (0, 0, 255)
colors['yellow'] = (255, 255, 0)
colors['purpule'] = (255, 0, 255)
colors['teal'] = (0, 128, 128)
colors['orange'] = (255, 115, 0)
colors['warmWhite'] = (255, 244, 229)

def rgbConvert(color):
    return (1-color[0]/255,1-color[1]/255,1-color[2]/255)

rColor, rValue = random.choice(list(colors.items()))
rColor2, rValue2 = random.choice(list(colors.items()))
rColor3, rValue3 = random.choice(list(colors.items()))
led.blink(onTime, 0, fadeIn, 0, rgbConvert(rValue), rgbConvert(rValue2), 1, False)
led.blink(onTime, 0, fadeIn, 0, rgbConvert(rValue3), rgbConvert(rValue), 1, False)
for i in range(changes):
    rColor, rValue = random.choice(list(colors.items()))
    led.blink(onTime, 0, fadeIn, 0, rgbConvert(rValue), rgbConvert(rValue3), 1, False)
    rColor3, rValue3 = random.choice(list(colors.items()))
    led.blink(onTime, 0, fadeIn, 0, rgbConvert(rValue3), rgbConvert(rValue), 1, False)
