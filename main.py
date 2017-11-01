#!/usr/bin/env python
import time
import signal
import sys
import os
import logging
import http.server
import socketserver
import threading

from classes.Pump import Pump
from classes.Moisture import Moisture
from classes.ManagerGPIO import ManagerGPIO
from classes.HTMLLogger import HTMLLogger

#: Global instances
_logger = None
_httpd = None
_port = 8000

def setup(title, version, filename="index.html", mode='w', level=logging.DEBUG):
    global _logger
    if _logger is None:
        _logger = HTMLLogger(filename=filename, mode=mode, title=title, version=version, level=level)


def signal_term_handler(signal, frame):
    destroy()


def destroy():
    global _logger
    global _httpd

    pumpA.destroy()
    pumpB.destroy()
    moist1.destroy()
    moist2.destroy()
    mgrGPIO.destroy()
    _httpd.server_close()
    _logger.info("APP ended")
    sys.exit(0)

def control():
    attempts = 0
    while True:
        if not moist1.isMoisty():  
            _logger.info("MOISTURE 1 is too dry, run PUMP A")          
            pumpA.execute()
            _logger.info("PUMP A stopped")
            attempts = attempts + 1
        else:
            attempts = 0
        
        if not moist2.isMoisty():  
            _logger.info("MOISTURE 2 is too dry, run PUMP B")          
            pumpB.execute()
            _logger.info("PUMP B stopped")
            attempts = attempts + 1
        else:
            attempts = 0

        if attempts > 10:
            _logger.error("ERROR: Many attempts to use the pump but no water")
            break        

        # time.sleep(5) # testing the system
        time.sleep(300) # check again after 5 minutes

    # end while
    os.kill(os.getpid(), signal.SIGTERM)

if __name__ == '__main__':     # Program start from here

    setup("Auto-Garden watering system", "v1.0-alpha")
    _logger.info("APP started")

    httpHandler = http.server.SimpleHTTPRequestHandler
    _httpd = socketserver.TCPServer(("", _port), httpHandler)
    print("HTTP server at port: ", _port)

    signal.signal(signal.SIGTERM, signal_term_handler)
    mgrGPIO = ManagerGPIO()
    pumpA = Pump(11, 5) # pin and duration in seconds
    pumpB = Pump(37, 5) # pin and duration in seconds
    moist1 = Moisture(13) # pin
    moist2 = Moisture(36) # pin
    _logger.info("APP initialized")

    try:
        t = threading.Thread(target=control)
        t.daemon = True
        t.start()

        _httpd.serve_forever()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()


 
