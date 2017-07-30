#!/usr/bin/env python
import time

from classes.Pump import Pump
from classes.ManagerGPIO import ManagerGPIO

if __name__ == '__main__':     # Program start from here
	mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 30) # pin, duration
	try:
        while True:
		    pumpA.execute()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		pumpA.destroy()
        ManagerGPIO.destroy()