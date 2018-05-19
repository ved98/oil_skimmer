import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time

skim1=19
skim2=21
ESC1=17
ESC2=27
ESC3=22
servo = 3

pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(skim1, GPIO.OUT)
GPIO.setup(skim2, GPIO.OUT)

front =7.5
left=5.0
right=10.0
fspeed =1000
tspeed=1200
rspeed=1200
rtspeed=1400

p = GPIO.PWM(servo, 50)
GPIO.setup(servo, GPIO.OUT)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
p.start(front)

def SKIM():
	GPIO.output(skim1,GPIO.HIGH)
	GPIO.output(skim2,GPIO.LOW)
def NOSKIM():
	GPIO.output(skim1,GPIO.LOW)
	GPIO.output(skim2,GPIO.LOW)	

def LEFT():
	p.ChangeDutyCycle(left)
	pi.set_servo_pulsewidth(ESC1, 0)
	pi.set_servo_pulsewidth(ESC3, rtspeed)
	pi.set_servo_pulsewidth(ESC2, tspeed)

def RIGHT():
	p.ChangeDutyCycle(right)
	pi.set_servo_pulsewidth(ESC1, tspeed)
	pi.set_servo_pulsewidth(ESC3, rtspeed)
	pi.set_servo_pulsewidth(ESC2, 0)

def STOP():
	p.ChangeDutyCycle(12.5)
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
	elif inp == "o":
	    SKIM()
	elif inp == "p":
	    NOSKIM()