import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time

ESC1=4
ESC2=17 
servo = 3

pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)



front =7.5
left=5.0
right=10.0
fspeed =1300
tspeed=1000
p = GPIO.PWM(servo, 50)
GPIO.setup(servo, GPIO.OUT)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
p.start(front)

def LEFT():
	p.ChangeDutyCycle(left)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def RIGHT():
	p.ChangeDutyCycle(right)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def STOP():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC2, 0)

def FRONT():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC1, fspeed)
	pi.set_servo_pulsewidth(ESC2, fspeed)

while True:
	inp = raw_input()
	if inp == "w":
	    FRONT()
	elif inp == "a":
	    LEFT()
	elif inp == "d":
	    RIGHT()
	elif inp == "s":
	    STOP()
	