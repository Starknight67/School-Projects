#Pacemaker V5
##Added Adjustable Metronome Functionality

# Pacemaker Code
#Importing things
from adafruit_circuitplayground.bluefruit import cpb
import time
import board
import digitalio
import neopixel
import math
from adafruit_ht16k33.segments import Seg7x4



#Button and LED stuff
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.5

#More variables

cooldown = 0

br = 10


def pxon(pixel):
    cpb.pixels[pixel] = ((10,10,10))

def pxoff(pixel):
    cpb.pixels[pixel] = ((0,0,0))

#Actual working bits
while True:
    if buttonA.value == True:
        starttime = time.monotonic()
        b1 = 0.01
        b2 = 0.01
        b3 = 0.01
        b4 = 0.01
        b5 = 0.01
        b6 = 0.01
        b7 = 0.01
        b8 = 0.01
        t = 0.01
        prev = 0
        while time.monotonic()-starttime < 60:
            x,y,z = cpb.acceleration
            accel = math.sqrt((x**2)+(y**2)+(z**2))
            now = time.monotonic() - starttime
            cooldown = (now - prev)
            if accel > 20 and cooldown > 0.2:
                cpb.pixels.fill((br,br,br))
                cpb.play_tone(880,0.1)
                pass
                prev = time.monotonic() - starttime
                b8=b7
                b7=b6
                b6=b5
                b5=b4
                b4=b3
                b3=b2
                b2=b1
                b1= time.monotonic()
                if b1!=b4:
                    bps = 7/((b1-b2)+(b2-b3)+(b3-b4)+(b4-b5)+(b5-b6)+(b6-b7)+(b7-b8))
                t=int(bps*60)
            else:
                cpb.pixels.fill((0,0,0))
                cpb.play_tone(0,0)


            display.print(t)
            print((b1,b2,b3,b4,b5,b6,t))
            print('Tempo is ', t,time.monotonic())
            time.sleep(0.025)
            if buttonA.value == True and buttonB.value == True:
                break
    else:
        if buttonB.value == True:
            time.sleep(0.5)
            t = 120
            while True:
                print('Tempo is ', t,time.monotonic())
                tempo = t
                if buttonA.value == True:
                    t = t-1
                if buttonB.value == True:
                    t = t+1
                if buttonA.value == True and buttonB.value == True:
                    break
                display.print(t)
                time.sleep(0.1)
            starttime = time.monotonic()
            bpm = tempo
            bps = (1/(bpm/60))
            w = bps*4
            h = bps*2
            q = bps
            e = bps/2
            s = bps/4
            while time.monotonic()-starttime < 180:
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
