import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time

pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)

ESC1=4
ESC2=17 
servo = 3

front =7.5
left=5
right=10
fspeed =1300
tspeed=1000

GPIO.setup(servo, GPIO.OUT)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
p.start(front)

def left():
	p.ChangeDutyCycle(left)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def right():
	p.ChangeDutyCycle(right)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def stop():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC2, 0)

def front():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC1, fspeed)
	pi.set_servo_pulsewidth(ESC2, fspeed)

while true:
	inp = raw_input()
	if inp == "w":
	    front()
	elif inp == "a":
	    left()
	elif inp == "d":
	    right()
	elif inp == "s":
	    stop()
	