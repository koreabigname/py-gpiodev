"""
Web : http://cihatkeser.com/servo-control-with-raspberry-pi-in-5-minutes-or-less/
Usage : python servo_sg90_basic.py
"""
from time import sleep
from sys import exit
import signal
import os

try:
	servo_num = int(raw_input("Which servo number? (NOT GPIO pin)"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

os.system('sudo servod')

try:
	while True:
		os.system("echo " + str(servo_num) + "=50 > /dev/servoblaster")
		sleep(1)
		os.system("echo " + str(servo_num) + "=230 > /dev/servoblaster")
		sleep(1)
except KeyboardInterrupt:
	pass
finally:
	print("Handling Ctrl+C")

