#Pacemaker V4
##Added Metronome Functionality
##Added GitHub Functionality

# Pacemaker Code
#Importing things
from adafruit_circuitplayground.bluefruit import cpb
import time
import board
import digitalio
import neopixel
import math

#Button and LED stuff
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

#More variables

cooldown = 0
prev = 0
br = 255

bpm = 120
bps = (1/(bpm/60))

w = bps*4
h = bps*2
q = bps
e = bps/2
s = bps/4

def pxon(pixel):
    cpb.pixels[pixel] = ((10,10,10))

def pxoff(pixel):
    cpb.pixels[pixel] = ((0,0,0))

#Actual working bits
while True:
    if buttonA.value == True:
        starttime = time.monotonic()
        while time.monotonic()-starttime < 60:
            x,y,z = cpb.acceleration
            accel = math.sqrt((x**2)+(y**2)+(z**2))
            now = time.monotonic() - starttime
            cooldown = (now - prev)
            if accel > 20 and cooldown > 0.2:
                cpb.pixels.fill((br,br,br))
                cpb.play_tone(880,0.1)
                prev = time.monotonic() - starttime
            else:
                cpb.pixels.fill((0,0,0))
                cpb.play_tone(0,0)
            time.sleep(0.05)
            print((now,prev,accel))
    else:
        if buttonB.value == True:
            starttime = time.monotonic()
            while time.monotonic()-starttime < 60:
                pxon(0)
                pxon(9)
                cpb.play_tone(880,s)
                time.sleep(e+s)
                pxoff(0)
                pxoff(9)
                pxon(1)
                pxon(8)
                cpb.play_tone(880,s)
                time.sleep(e+s)
                pxoff(1)
                pxoff(8)
                pxon(2)
                pxon(7)
                cpb.play_tone(880,s)
                time.sleep(e+s)
                pxoff(2)
                pxoff(7)
                pxon(3)
                pxon(6)
                cpb.play_tone(880,s)
                time.sleep(e+s)
                pxoff(3)
                pxoff(6)
