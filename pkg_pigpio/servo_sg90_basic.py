"""
Web : http://abyz.co.uk/rpi/pigpio/python.html
Usage : sudo pigpiod
        python servo_sg90_basic.py
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
pi.set_servo_pulsewidth(gpio_pin_num, 0)

try:
	while True:
		pi.set_servo_pulsewidth(gpio_pin_num, 500)
		sleep(1)
		pi.set_servo_pulsewidth(gpio_pin_num, 2500)
		sleep(1)
except KeyboardInterrupt:
	pi.set_servo_pulsewidth(gpio_pin_num, 0)
	pi.stop()
finally:
	print("Handling Ctrl+C")

