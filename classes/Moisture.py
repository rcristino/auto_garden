#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class Moisture:

    def __init__(self, pin):
        self.pin = pin
        self.setup()

    def destroy(self):
        GPIO.remove_event_detect(self.pin)
        print("moisture DESTROY: " + str(self.pin))

    def setup(self):
        GPIO.setup(self.pin, GPIO.IN)   # Set pin mode is input
        # get input from gpio pin when the pin goes HIGH or LOW
        GPIO.add_event_detect(self.pin, GPIO.BOTH, bouncetime=300)
        GPIO.add_event_callback(self.pin, self.callback)
        print("moisture INIT: " + str(self.pin))

    def callback(self, pin):
        if GPIO.input(pin):
            print("moisture DETECTED: " + str(self.pin)) 
        else:
            print("moisture NOT DETECTED: " + str(self.pin)) 
