"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/recipes.html#led-with-variable-brightness
Usage : python led_brightness_basic.py
"""
from gpiozero import PWMLED
from time import sleep
from sys import exit

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

led = PWMLED(gpio_pin_num)

while True:
	led.value = 0  # off
	sleep(1)
	led.value = 0.5  # half brightness
	sleep(1)
	led.value = 1  # full brightness
	sleep(1)

