import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio
import RPi.GPIO as GPIO
import time
import cv2
import sys
import numpy as np
import skimage.measure
import picamera
import io

ESC1=18
ESC2=17 
servo = 3
camera =8 

stream = io.BytesIO()
pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(camera, GPIO.OUT)


front =7.5
left=5.0
right=10.0
fspeed =1300
tspeed=1000

p = GPIO.PWM(servo, 50)
c = GPIO.PWM(camera, 50)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
p.start(front)
c.start(front)

def readImage(stream): 
    data=np.fromstring(stream.getvalue(), dtype=np.uint8)
    img=cv2.imdecode(data,1)
    #img = cv2.imread("test.jpg", 1) # load image, 1 means load in RGB format
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to hsv

    lower_range = np.array([0, 0, 150], dtype=np.uint8) #lower bound of color to detect
    upper_range = np.array([255, 70, 255], dtype=np.uint8) #upper bound of color to detect

    #create a mask for the image
    mask = cv2.inRange(hsv, lower_range, upper_range)
    kernel = np.ones((7,7),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations = 2)
    mask = cv2.medianBlur(mask, 15)
    mask = skimage.measure.block_reduce(mask, (5, 5), np.max)
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
    cv2.imwrite("test_mask.jpg", mask)
    return res
    # mask = skimage.measure.block_reduce(mask, (5, 5), np.max)

    # cv2.imshow('mask',mask)
    
    # cv2.imshow('image', img)

    # while(1):
    #   k = cv2.waitKey(0)
    #   if(k == 27):
    #       break

    # cv2.destroyAllWindows()

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

angles = np.array([7.5,8.5,9.5,10.5,11.5,12.5,6.5,5.5,4.5,3.5,2.5])
ptr=0
with picamera.PiCamera() as cam1:
    cam1.resolution = (200,200)
    cam1.start_preview()
    time.sleep(2)
    while True:
        print("angle="+str((angles[ptr]-2.5)*18-90))
        c.ChangeDutyCycle(angles[ptr])
        time.sleep(0.5)
        cam1.capture(stream , format = 'jpeg')
        res=readImage(stream)
        if res==0:
            FRONT()
        else :
            ptr+=1
        if ptr == len(angles):
            ptr=0
	
	