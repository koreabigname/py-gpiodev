"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/recipes.html#led-with-variable-brightness
Usage : python led_brightness_alternatively.py
"""
from gpiozero import PWMLED
from signal import pause
from sys import exit

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

led = PWMLED(gpio_pin_num)

led.pulse()

pause()

