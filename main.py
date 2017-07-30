#!/usr/bin/env python
import time

from classes.Pump import Pump
from classes.ManagerGPIO import ManagerGPIO

if __name__ == '__main__':     # Program start from here
    mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 3) # pin and duration
    try:
        #while True:
        pumpA.execute()
        
        pumpA.destroy()
        mgrGPIO.destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        pumpA.destroy()
        mgrGPIO.destroy()