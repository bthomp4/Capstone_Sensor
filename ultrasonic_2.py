#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Ultrasonic related posts:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
#
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# -----------------------
# Import required Python libraries
# -----------------------
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------
def measure1():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER1, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER1, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO1)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO1)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * speedSound)/2

  return distance

def measure_average1():
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure1()
  time.sleep(0.1)
  distance2=measure1()
  time.sleep(0.1)
  distance3=measure1()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance
  
def measure2():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER2, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER2, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO2)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO2)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * speedSound)/2

  return distance

def measure_average2():
  # This function takes 3 measurements and
  # returns the average.

  distance1=measure2()
  time.sleep(0.1)
  distance2=measure2()
  time.sleep(0.1)
  distance3=measure2()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER1 = 23
GPIO_ECHO1    = 24
GPIO_LED1     = 17
GPIO_LED2     = 27
GPIO_TRIGGER2 = 5
GPIO_ECHO2    = 6

# Speed of sound in in/s at temperature
speedSound = 13500 # in/s

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.setup(GPIO_LED1,GPIO.OUT)     # LED 1

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_LED1, False)

# Allow module to settle
time.sleep(0.5)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
  while True:
    distance = measure_average1()
    # printing distance for know will eventually delete this
    print("Distance Sensor 1: %d inches" %distance)
    # if there is something less than 4 ft away from sensor
    if distance <= 48:
        # Turn on led 1
        GPIO.output(GPIO_LED1, True)
    else:
        GPIO.output(GPIO_LED1, False)
    
    distance = measure_average2()
    print("Distance Sensor 1: %d inches" % distance)
    if distance <= 48:
        GPIO.output(GPIO_LED2, True)
    else:
        GPIO.output(GPIO_LED2, False)
    
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()