import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time
import cv2
import sys
import numpy as np
# import skimage.measure

def readImage(): 
    img = cv2.imread(sys.argv[1], 1) # load image, 1 means load in RGB format
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to hsv

    lower_range = np.array([0, 0, 150], dtype=np.uint8) #lower bound of color to detect
    upper_range = np.array([255, 70, 255], dtype=np.uint8) #upper bound of color to detect

    #create a mask for the image
    mask = cv2.inRange(hsv, lower_range, upper_range)
    kernel = np.ones((7,7),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations = 2)
    mask = cv2.medianBlur(mask, 15)
    rows = mask.shape[0]
    cols = mask.shape[1]
    print rows
    print cols
    res = 0
    total = 0
    for x in xrange(0, rows-10, 10):
            for y in xrange(0, cols-10, 10):
                    count=0
                    for i in xrange(0, 10):
                            for j in xrange(0, 10):
                                    if mask[x+i, y+j] == 0:
                                            count += 1
                    if count >= 30:
                            total += count
                    if total >= 15000:
                            res = 1
    print res
    print total
    print total >= rows*cols/4
    print rows*cols/4
    return res
    # mask = skimage.measure.block_reduce(mask, (5, 5), np.max)

    # cv2.imshow('mask',mask)
    cv2.imwrite(sys.argv[1] + "_mask.jpg", mask)
    # cv2.imshow('image', img)

    # while(1):
    # 	k = cv2.waitKey(0)
    # 	if(k == 27):
    # 		break

    # cv2.destroyAllWindows()


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
	