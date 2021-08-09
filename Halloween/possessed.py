#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
class detector(object):
 def __init__(self, sensor):
 self.callBacks = []
 self.sensor = sensor
 self.currState = False
 self.prevState = False
 GPIO.setmode(GPIO.BOARD)
                GPIO.setup(self.sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def read(self):
 self.prevState = self.currState
 self.currState = GPIO.input(self.sensor)
def printState(self):
 print( "GPIO pin {0} is {1}".format(self.sensor, "HIGH" if self.currState else "LOW"))
def subscribe(self, callBack):
 self.callBacks.append(callBack)
def callBack(self, state):
 for fn in self.callBacks:
                        fn(state)
def start(self):
 try:
 self.read()
 self.printState()
 while True:
 self.read()
 if self.currState != self.prevState:
 self.printState()
 self.callBack(self.currState)
                                 time.sleep(.1)
 #Since fbi doesn't restore the console correctly when the application is exited we do a little clean up and handle the KeyboardInterrupt event.
except (KeyboardInterrupt, SystemExit):
 os.system('stty sane')

scare.py

#!/usr/bin/python
import subprocess as sp
import time
import os
from pirDetect import *
import sys
video = ["omxplayer", "filename", "-o", "both", "--win", "0 0 1280 720", "--aspect-mode", "fill", "--no-osd", "--orientation" ,"180","--vol", "-600"]
scareFile = "/home/pi/Projects/Halloween/ScareMedia/{0}ScareV.mp4".format(sys.argv[1])
print(scareFile)
def onMotion(currState):
 if currState:
        video[1] = scareFile
        subVideo = sp.Popen(video)
 while subVideo.poll() is None:
            time.sleep(.1)
def showImage():
    os.system("sudo fbi -T 1 -d /dev/fb0 -noverbose -once /home/pi/Projects/Halloween/ScareMedia/{0}Start.png".format(
        sys.argv[1]))
showImage()
objDetect = detector(7)
objDetect.subscribe(onMotion)
objDetect.start()
os.system("sudo killall -9 fbi")

