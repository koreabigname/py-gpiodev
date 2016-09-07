"""
Web : https://gpiozero.readthedocs.io/en/v1.3.1/recipes.html#button-controlled-camera
      https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/
      http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera
Usage : python button_camera_basic.py
"""
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from sys import exit
import signal

try:
	gpio_pin_num = int(raw_input("Which gpio pin?"))
except ValueError:
	print "Oops! That was no valid number. Try again.."
	exit()

button = Button(gpio_pin_num, pull_up=False)

def button_pressed():
	current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
	camera = PiCamera()
	camera.capture('/home/pi/%s.jpg' % current_time)
	camera.close()

button.when_pressed = button_pressed

try:
	signal.pause()
except KeyboardInterrupt:
	pass
finally:
	print("Handling Ctrl+C")

