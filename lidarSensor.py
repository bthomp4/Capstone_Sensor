#!/usr/bin/python
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
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
def measure():
    # This function measures a distance
    GPIO.output(GPIO_TRIGGER, True)
    # Wait 10us
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    stop = time.time()

    elapsed = stop - start # every 10 microseconds = 1 cm
    distance = elapsed * (10  ** 5) # in cm
    distance = distance  * 0.0328084 # in feet

    return distance


def measure_average():
    # This function takes 3 measurements and
    # returns the average.
    n = 50
    for i in range(0,n):
        sum_measurement = sum_measure + measure()
        time.sleep(0.05)
    return sum_measure/n
    # No for loop because I want to make Ben angry
#    distance1 = measure()
#    time.sleep(0.05)
#    distance2 = measure()
#    time.sleep(0.05)
#    distance3 = measure()
#    time.sleep(0.05)
#    distance4 = measure()
#    time.sleep(0.05)
#    distance5 = measure()
#    time.sleep(0.05)
#    distance6 = measure()
#    time.sleep(0.05)
#    distance7 = measure()
#    time.sleep(0.05)
#    distance8 = measure()
#    time.sleep(0.05)
#    distance9 = measure()
#    time.sleep(0.05)
#    distance10 = measure()
#    time.sleep(0.05)
#    distance11 = measure()
#    time.sleep(0.05)
#    distance12 = measure()
#    distance = distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10 + distance11 + distance12
#    distance = distance / 12
#    return distance


# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 20

# Speed of sound in in/s at temperature
speedLight = (9.8 * (10 ** 8))  # ft/s

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger 1
GPIO.setup(GPIO_ECHO, GPIO.IN)  # Echo 1

# Set trigger to True (high)
GPIO.output(GPIO_TRIGGER, True)
#GPIO.output(GPIO_LED, False)

# Allow module to settle
time.sleep(0.5)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
    print("Lidar Distance:")
    while True:
        distance = measure_average()
        # printing distance for know will eventually delete this
        print("Distance: %d feet" %distance)
        # if there is something less than 4 ft away from sensor
        #if distance1 <= 48:
        #    # Turn on led 1
        #    GPIO.output(GPIO_LED1, True)
        #else:
        #    GPIO.output(GPIO_LED1, False)

        time.sleep(1)

except KeyboardInterrupt:
    # User pressed CTRL-C
    # Reset GPIO settings
    GPIO.cleanup()
