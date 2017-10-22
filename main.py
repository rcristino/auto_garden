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
    moist1 = Moisture(13) # pin
    try:
        #while True:

        #pumpA.execute()

        time.sleep(5) # for testing

        pumpA.destroy()
        moist1.destroy()
        mgrGPIO.destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        pumpA.destroy()
        moist1.destroy()
        mgrGPIO.destroy()