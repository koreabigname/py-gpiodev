"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/recipes.html#led
Usage : python led_blink_alternatively.py
"""
from gpiozero import LED
from signal import pause
from sys import exit

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

led = LED(gpio_pin_num)

led.blink()

pause()
