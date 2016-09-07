"""
Web : https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
Usage : python led_blink_basic.py
"""
import RPi.GPIO as GPIO
from time import sleep
from sys import exit
import signal

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_num, GPIO.OUT)

try:
	while True:
		GPIO.output(gpio_pin_num, GPIO.HIGH)
		sleep(1)
		GPIO.output(gpio_pin_num, GPIO.LOW)
		sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	print("Handling Ctrl+C")

