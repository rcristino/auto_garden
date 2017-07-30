#!/usr/bin/env python
import RPi.GPIO as GPIO

class ManagerGPIO:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        print("ManagerGPIO INITª)

    def destroy(self):
        GPIO.cleanup()
        print("ManagerGPIO DESTROY")