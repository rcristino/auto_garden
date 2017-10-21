#!/usr/bin/env python
import time
from flask import Flask
from gui import gui

from classes.Pump import Pump
from classes.Moisture import Moisture
from classes.ManagerGPIO import ManagerGPIO

if __name__ == '__main__':     # Program start from here

    # gui.run(debug=True) # gui app

    mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 3) # pin and duration
    moistA = Moisture(13) # pin
    try:
        #while True:

        #pumpA.execute()
        
        time.sleep(5) # for testing

        pumpA.destroy()
        moistA.destroy()
        mgrGPIO.destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        pumpA.destroy()
        moistA.destroy()
        mgrGPIO.destroy()