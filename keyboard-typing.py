import usb_hid
#from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
from adafruit_hid.mouse import Mouse
import board
import digitalio

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


str1 = '''import math as m
'''

str2 = '''
print('Hello, world!')

print('PI is ' + str(m.pi))
'''

time.sleep(30.0)

layout.write(str1)

while True:
    layout.write(str2)
    time.sleep(30.0)
