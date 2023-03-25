# Pacemaker Code
#Importing things
from adafruit_circuitplayground.bluefruit import cpb
import time
import board
import digitalio
import neopixel
import math

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!


#Button and LED stuff
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

# enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

a = audioio.AudioOut(board.SPEAKER)

def PLAY_SOUND(filename):
    print("Playing Sound")
    f = open(filename, "rb")
    wav = audioio.WaveFile(f)
    a.play(wav)
    while a.playing:
        pass
    f.close()
    return

cooldown = 0
prev = 0
br = 255

##RickRoll Parameters
A3 = 220
Bb3= 223.08
B3 = 246.94
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392
A4 = 440
Bb4= 466.16
B4 = 493.88
C5 = 523.25
D5 = 587.33
E5 = 659.25
F5 = 698.46
G5 = 784
A5 = 880
Bb5= 932.33
B5 = 987.77
C6 = 1046.5
D6 = 1174.66
E6 = 1318.51
F6 = 1396.91
G6 = 1567.98
A6 = 1760
##Choosing Tempo
bpm = 114
bps = (1/(bpm/60))

##Determining length of notes
w = bps*4
h = bps*2
q = bps
e = bps/2
s = bps/4

#Making play and rest functions
def play(note, length):
    cpb.pixels.fill((br,br,br))
    cpb.play_tone(note, length)
    cpb.pixels.fill((0,0,0))
def rest(length):
    time.sleep(length)

while True:
    if buttonA.value == True:
        while time.monotonic()-starttime < 60:
            starttime = time.monotonic()
            x,y,z = cpb.acceleration
            accel = math.sqrt((x**2)+(y**2)+(z**2))
            now = time.monotonic() - starttime
            cooldown = (now - prev)
            if accel > 20 and cooldown > 0.15:
                cpb.pixels.fill((br,br,br))
                #cpb.play_tone(880,0.1)
                PLAY_SOUND("airhorn.wav")
                prev = time.monotonic() - starttime
            else:
                cpb.pixels.fill((0,0,0))
                cpb.play_tone(0,0)
            time.sleep(0.01)
            print((now,prev,accel))
    else:
        if buttonB.value == True:
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas1
            play(A4,e+s)
            play(A4,e+s)
            play(G4,q+e)
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas2
            play(G4,e+s)
            play(G4,e+s)
            play(F4,e+s)
            play(E4,s)
            play(D4,e)
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas3
            play(F4,q)
            play(G4,e)
            play(E4,e+s)
            play(D4,s)
            play(C4,q)
            play(C4,e)
            #meas4
            play(G4,q)
            play(F4,q+e)
            rest(e)
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas5
            play(A4,e+s)
            play(A4,e+s)
            play(G4,q+e)
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas6
            play(C5,q)
            play(E4,e)
            play(F4,e+s)
            play(E4,s)
            play(D4,e)
            play(C4,s)
            play(D4,s)
            play(F4,s)
            play(D4,s)
            #meas7
            play(F4,q)
            play(G4,e)
            play(E4,e+s)
            play(D4,s)
            play(C4,q)
            play(C4,e)
            #meas8
            play(G4,q)
            play(F4,h)
