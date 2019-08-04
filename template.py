#!/usr/bin/python3
"""
Python Practical Template
Joshua Eybers
Readjust this Docstring as follows:
Names: <Joshua>
Student Number: <EYBJOS001>
Prac: <1>
Date: <04/08/1998>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product

# Logic that you write
a = 0 # create counter int

c=0   # create binary counter

def convert(d):
	global c
	global b
	c='{0:03b}'.format(a)  # convert a to 3 bit binary


def add(channel):
	global a
	a+=1		       # increment counter
	if a ==	8:	       
		a=0	       # reset counter when it reaches 8
	convert(a)
	b = tuple(c)	       # convert c to a tuple
	n1= int(b[0])	       # convert first bit of c to int
	n2= int(b[1])	       # convert 2nd bit of c to int
	n3= int(b[2])	       # convert 3rd bit of c to int
	GPIO.output(chan_out,(n1,n2,n3))	# display c on LED

	print(tuple(c))
def subtract(channel):
	global a
	a-=1
	if a ==	-1:	
		a=7	       # if resets a when it reaches -1
	convert(a)
	b=tuple(c)
	n1 = int(b[0])	       # same ass add function
	n2 = int(b[1])
	n3 = int(b[2])
	GPIO.output(chan_out,(n1,n2,n3))
	
def main():
    time.sleep(0.001)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	GPIO.setmode(GPIO.BCM)								# set up pins to BCM  	
	chan_in	=[23,24]								# create an aray list for inputs
	chan_out = [17,27,22]								# create an aray list for outputs
	GPIO.setup(chan_out, GPIO.OUT, initial=GPIO.LOW)				# init pins 17,27,22 as output pins and set initial value to 0
	GPIO.setup(chan_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)			# init pins 23,24 as pull down input pins 
	GPIO.add_event_detect(23, GPIO.RISING, callback=add, bouncetime=200)		# event detention for add when pin 23 recieves a 1
	GPIO.add_event_detect(24, GPIO.RISING, callback=subtract, bouncetime=200)	# event detection for subtract when pin 24 recieves a 1
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
