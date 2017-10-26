#!/usr/bin/env python
import time
import signal
import sys
import logging

from classes.Pump import Pump
from classes.Moisture import Moisture
from classes.ManagerGPIO import ManagerGPIO
from classes.HTMLLogger import HTMLLogger

#: Global logger instance
_logger = None

def setup(title, version, filename="log.html", mode='w', level=logging.DEBUG):
    global _logger
    if _logger is None:
        _logger = HTMLLogger(filename=filename, mode=mode, title=title, version=version, level=level)


def signal_term_handler(signal, frame):
    destroy()


def destroy():
    global _logger
    pumpA.destroy()
    moist1.destroy()
    mgrGPIO.destroy()
    _logger.info("APP ended")
    sys.exit(0)

if __name__ == '__main__':     # Program start from here

    setup("Auto-Garden watering system", "v1.0-alpha")
    signal.signal(signal.SIGTERM, signal_term_handler)

    _logger.info("APP started")

    mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 5) # pin and duration
    moist1 = Moisture(13) # pin

    _logger.info("APP initialized")

    try:
        while True:
            if not moist1.isMoisty():  
                _logger.info("MOISTURE 1 is too dry, run PUMP A")          
                pumpA.execute()
                _logger.info("PUMP A stopped") 

            time.sleep(300) # check again after 5 minutes

        # end while
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

 
