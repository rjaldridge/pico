
# needs circuitpython installed
# needs adafruit-circuitpython-hid library downloaded and installed 

import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(5)

while True:
	led.value = True
	mouse.move(x=100)
	led.value = False
	time.sleep(30.0)
	led.value = True
	mouse.move(x=-100)
	led.value = False
	time.sleep(30.0)
	
	