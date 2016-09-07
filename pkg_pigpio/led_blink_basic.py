"""
Web : http://abyz.co.uk/rpi/pigpio/python.html
Usage : sudo pigpiod
        python led_blink_basic.py
"""
import pigpio 
from time import sleep
from sys import exit
import signal

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

pi = pigpio.pi()

try:
	while True:
		pi.write(gpio_pin_num, 1)
		sleep(1)
		pi.write(gpio_pin_num, 0)
		sleep(1)
except KeyboardInterrupt:
	pi.stop()
finally:
	print("Handling Ctrl+C")

