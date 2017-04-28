#!/usr/bin/python

from gpiozero import MotionSensor
from time import *
import logging

def logger():
# Configure Logging Format and Location
 logging.basicConfig(level=logging.INFO, format='%(asctime)s, %(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S',
                    filename='/home/pi/scripts/motion.txt',
                    filemode='w')
 motion = "Detected"
 # Log the motion data and wait until the next read
 logging.info(str(motion))
 return;

#Connect Motion Sensor to 5V, Gnd and GPIO17
pir = MotionSensor(17)
while True:
    if pir.motion_detected:
        print("Motion detected!")
        logger()
        sleep(5)
