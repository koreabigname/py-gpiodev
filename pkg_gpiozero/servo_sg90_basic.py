"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/api_output.html?highlight=servo#servo
Usage : python servo_sg90_basic.py
"""
from gpiozero import Servo 
from time import sleep
from sys import exit
import signal

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

servo = Servo(gpio_pin_num, min_pulse_width=0.0005, max_pulse_width=0.0025)

try:
	while True:
		servo.min()
		sleep(1)
		servo.mid()
		sleep(1)
		servo.max()
		sleep(1)
		servo.mid()
		sleep(1)
except KeyboardInterrupt:
	pass
finally:
	print("Handling Ctrl+C")

