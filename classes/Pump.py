#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class Pump:

    def __init__(self, pin, duration):
        self.pin = pin
        self.duration = duration
        self.setup()

    def destroy(self):
        GPIO.output(self.pin, GPIO.HIGH)     # pump off
        print("pump: DESTROY: " + str(self.pin))

    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)   # Set pin mode is output
        GPIO.output(self.pin, GPIO.HIGH) # Set pin high(+3.3V) to off
        print("pump: INIT: " + str(self.pin))

    def execute(self):
        print("pump: ON: " + str(self.pin))
        GPIO.output(self.pin, GPIO.LOW)  # pump on
        time.sleep(self.duration)
        print("pump: OFF: " + str(self.pin))
        GPIO.output(self.pin, GPIO.HIGH) # pump off
