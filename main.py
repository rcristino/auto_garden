#!/usr/bin/env python
import time
import signal
import sys

from classes.Pump import Pump
from classes.Moisture import Moisture
from classes.ManagerGPIO import ManagerGPIO


def signal_term_handler(signal, frame):
    destroy()

def destroy():
    pumpA.destroy()
    moist1.destroy()
    mgrGPIO.destroy()
    sys.exit(0)

if __name__ == '__main__':     # Program start from here

    signal.signal(signal.SIGTERM, signal_term_handler)

    mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 5) # pin and duration
    moist1 = Moisture(13) # pin
    try:
        while True:
            if not moist1.isMoisty():                
                pumpA.execute()

            time.sleep(300) # check again after 5 minutes

        # end while
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

 
