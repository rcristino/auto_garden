# Auto-Garden watering system

## The Goal
It is to create a watering system which monitors the moisture level from the ground and when the level is too low, it is hable to water the plants.
All watering activity should be tracked and easy access. It should include safety guards to not allow the pumps running with a empty deposit or in case the watering activity has no effect on the moisture level.
The entire system shall be self contained and portable.

 ## The components

 1. Two plactic boxes, one works as a water tank and the second to store the electric components
 2. [Raspberry Pi 2 Model B](https://en.wikipedia.org/wiki/Raspberry_Pi)
 3. [Soil Hygrometer Humidity Detection Module Soil Moisture Water Sensor](https://www.ebay.de/itm/Soil-Hygrometer-Humidity-Detection-Module-Soil-Moisture-Water-Sensor-For-arduino/232462821136?hash=item361fdd2710:g:RtMAAOSweQBZn8ym)
 4. [Relay Module](http://www.ebay.de/itm/TWO-PCS-4-Kanale-Channel-5V-Relais-Relay-Module-fur-Arduino-UNO-Mega-DSP-AVR-ARM/231156577754?hash=item35d20175da:g:t9MAAOSwBahVQJPQ)
 5. [Aquarium Pump](https://www.amazon.de/gp/product/B00G3YSDCE/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
 6. Cables, tubes, switches, etc

 ## How to run?
 Make sure all setup describe here is ready.
 Clone this repo in your rasberry pi and using the terminal execute:

     > ./run.sh

This program is based on python3 and uses GPIO modules as well as SimpleHttpServer for the logging. Make sure all this modules have been previously installed (pip3 command) 

The logging where is the watering activity is tracked can be reach in any browser poiting to the rasberry pi address

    http://127.0.0.1:8000

## Notes

Watering intervals and pins configuration are configured in main.py file

## References
[modmypi](https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial)
[pi4j](http://pi4j.com/pins/model-2b-rev1.html)