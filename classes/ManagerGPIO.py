#!/usr/bin/env python
import RPi.GPIO as GPIO

class ManagerGPIO:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        print("managerGPIO: INIT")

    def destroy(self):
        GPIO.cleanup()
        print("managerGPIO: DESTROY")