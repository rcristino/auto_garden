#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class Pump:

    def __init__(self, pin, duration):
        self.pin = pin
        self.duration = duration
        self.setup()

    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)   # Set pin mode is output
        GPIO.output(self.pin, GPIO.HIGH) # Set pin high(+3.3V) to off
        print("pump INITª + self.pin)

    def destroy(self):
        GPIO.output(self.pin, GPIO.HIGH)     # pump off
        GPIO.cleanup() 
        print("pump DESTROY + self.pin)

    def execute():
        print("pump ONª + self.pin)
        GPIO.output(self.pin, GPIO.LOW)  # pump on
        time.sleep(self.duration)
        print("pump OFFª + self.pin)
        GPIO.output(self.pin, GPIO.HIGH) # pump off
