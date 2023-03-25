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

#More variables
starttime = time.monotonic()
cooldown = 0
prev = 0
while time.monotonic()-starttime < 60:
    x,y,z = cpb.acceleration
    accel = math.sqrt((x**2)+(y**2)+(z**2))
    now = time.monotonic() - starttime
    cooldown = (now - prev)
    if accel > 18 and cooldown > 0.2:
        cpb.pixels.fill((50,50,50))
        cpb.play_tone(880,0.05)
        prev = time.monotonic() - starttime
    else:
        cpb.pixels.fill((0,0,0))
        cpb.play_tone(0,0)
    time.sleep(0.05)
    print(accel,now,prev)
