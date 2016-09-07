"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/recipes.html#button
Usage : python button_basic.py
"""
from gpiozero import Button
from sys import exit
import signal

def button_pressed():
	print("Button is pressed");

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

button = Button(gpio_pin_num, pull_up=False)
button.when_pressed = button_pressed

try:
	signal.pause()
except KeyboardInterrupt:
	pass
finally:
	print("Handling Ctrl+C")

