import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time

ESC1=17
ESC2=18 
ESC3=27
servo = 3

pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)

front =7.5
left=5.0
right=10.0
fspeed =780
tspeed=780
rspeed=780

p = GPIO.PWM(servo, 50)
GPIO.setup(servo, GPIO.OUT)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
p.start(front)

def LEFT():
	p.ChangeDutyCycle(left)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC3, rspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def RIGHT():
	p.ChangeDutyCycle(right)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC3, rspeed)
	pi.set_servo_pulsewidth(ESC2, 0)

def STOP():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC3, 0)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC2, 0)

def BACK():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC3, rspeed)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC2, 0)

def FRONT():
	p.ChangeDutyCycle(front)
	pi.set_servo_pulsewidth(ESC3, 0)
	pi.set_servo_pulsewidth(ESC2, fspeed)
	pi.set_servo_pulsewidth(ESC1, fspeed)
        #time.sleep(20)
        
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
	elif inp == "z":
	    BACK()
	