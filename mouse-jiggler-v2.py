
# needs circuitpython installed
# needs adafruit-circuitpython-hid library downloaded and installed 

import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

slp = 58.0 # Delay before moving the mouse
dst = 1    # Distance to move the mouse

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

time.sleep(slp)

while True:
	mouse.move(x=dst)
	time.sleep(slp)
	mouse.move(x=(-1 * dst))
	time.sleep(slp)
    
    
	
	