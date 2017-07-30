#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off

def loop():
	duration = 30
	if True:
		print '...pump on'
		GPIO.output(LedPin, GPIO.LOW)  # pump on
		time.sleep(duration)
		print 'pump off...'
		GPIO.output(LedPin, GPIO.HIGH) # pump off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # pump off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


