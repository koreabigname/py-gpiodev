"""
Web : https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
Usage : python servo_sg90_basic.py
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
pwm = GPIO.PWM(gpio_pin_num, 50)
pwm.start(0)

try:
	while True:
		pwm.ChangeDutyCycle(2)
		sleep(1)
		pwm.ChangeDutyCycle(7)
		sleep(1)
		pwm.ChangeDutyCycle(12) 
		sleep(1)
except KeyboardInterrupt:
	pwm.stop()
finally:
	print("Handling Ctrl+C")

