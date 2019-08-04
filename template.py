#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product

# Logic that you write
a = 0

c=0

def convert(d):
	global c
	global b
	c='{0:03b}'.format(a)


def add(channel):
	global a
	a+=1
	if a == 8:
		a=0
	convert(a)
	b = tuple(c)
	n1= int(b[0])
	n2= int(b[1])
	n3= int(b[2])
	GPIO.output(chan_out,(n1,n2,n3))

	print(tuple(c))
def subtract(channel):
	global a
	a-=1
	if a == -1:
		a=7
	convert(a)
	b=tuple(c)
	n1 = int(b[0])
	n2 = int(b[1])
	n3 = int(b[2])
	GPIO.output(chan_out,(n1,n2,n3))
	
def main():
    time.sleep(0.001)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	GPIO.setmode(GPIO.BCM)
	chan_in =[23,24]
	chan_out = [17,27,22]
	GPIO.setup(chan_out, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(chan_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(23, GPIO.RISING, callback=add, bouncetime=200)
	GPIO.add_event_detect(24, GPIO.RISING, callback=subtract, bouncetime=200)
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
