""""
This was the code I used when testing the sensors initially, it should work on the pi.
For reference I used the tutorial found here: https://learn.adafruit.com/using-mcp23008-mcp23017-with-circuitpython/python-circuitpython
This has the needed directories. I am not sure if this tutorial goes over connecting multiple busses. 
To find the address of the bus you need to set up the MCP23017 by setting some arrangement to ground. (A0, A1, A2 pins to ground is 0x20),
There is some guide on this in the tutorial.

I used this tutorial: https://www.youtube.com/watch?v=Kx87ldgD6Sg help figure out how to connect it.
"""
import time
import board
import busio
import digitalio
import RPi.GPIO as gpio


from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)

mcp1 = MCP23017(i2c, address=0x20)
#mcp2 = MCP23017(i2c, address=0x27)

pin0 = mcp1.get_pin(7)
#pin1 = mcp2.get_pin(7)
#pin2 = mcp2.get_pin(8)

pin0.switch_to_input()
#pin1.switch_to_input()
#pin2.switch_to_input()

i = 0
while True:
    print("Pin 0 (mcp1):", pin0.value)
    print(i, "--------------", i)
    i += 1
    time.sleep(1)
