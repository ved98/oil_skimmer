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
import socket

HOST = '10.7.9.9'    # The remote host
PORT = 50007
ESC1=18
ESC2=17 
servo = 3
camera =8
skim1=19
skim2=21
ESC3=22
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pi = pigpio.pi();
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(camera, GPIO.OUT)


front =7.5
left=5.0
right=10.0
fspeed =1000
tspeed=1200
rspeed=1200
rtspeed=1400

p = GPIO.PWM(servo, 50)
c = GPIO.PWM(camera, 50)
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
p.start(front)
c.start(front)

def blackPercentage():
    count1=0
    count2=0
    for x in xrange(0, rows):
        for y in xrange(0, cols):
            if mask[x][y] == 255:
                count1+=1
            else:
                count2+=1

    print count2*100/(count1+count2)

    count1=0
    count2=0
    for x in xrange(0, rows):
        for y in xrange(0, cols):
            if mask2[x][y] == 255:
                count1+=1
            else:
                count2+=1
                
    return count2*100/(count1+count2)

def detectBoundaries():
    for x in xrange(0, cols):
        flag = -1
        for y in xrange(0, rows):
            if(mask_brick[y][x] == 255):
                # print y
                flag = y
                break
        if flag != -1:
            # print flag
            for z in xrange(0, flag-1):
                mask_brick[z][x] = 127
                mask[z][x] = 127


def readImage(stream): 
    global inm
    data=np.fromstring(stream.getvalue(), dtype=np.uint8)
    img=cv2.imdecode(data,1)
    cv2.imwrite("data/"+str(inm)+"test.jpg", img)
    #img = cv2.imread("test.jpg", 1) # load image, 1 means load in RGB format
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to hsv

    lower_range = np.array([0, 0, 150], dtype=np.uint8) #lower bound of color to detect
    upper_range = np.array([255, 70, 255], dtype=np.uint8) #upper bound of color to detect

    lower_range_brick_color = np.array([0, 100, 100], dtype=np.uint8) #lower bound of brick color to detect
    upper_range_brick_color = np.array([32, 255, 255], dtype=np.uint8) #upper bound of brick color to detect

    #create a mask for the image
    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask2 = cv2.inRange(hsv, lower_range, upper_range)
    mask_brick = cv2.inRange(hsv, lower_range_brick_color, upper_range_brick_color)
    kernel = np.ones((3,3),np.uint8)
    mask2 = cv2.dilate(mask2,kernel,iterations = 1)
    mask2 = cv2.medianBlur(mask2, 5)
    detectBoundaries()
    oil=blackPercentage()
    #mask = skimage.measure.block_reduce(mask, (5, 5), np.max)
    cv2.imwrite(str(inm)+"test_mask.jpg", mask)
    inm+=1
    if oil>30 :
        res=1
    else :
        res= 0
    return res
    # mask = skimage.measure.block_reduce(mask, (5, 5), np.max)

    # cv2.imshow('mask',mask)
    
    # cv2.imshow('image', img)

    # while(1):
    #   k = cv2.waitKey(0)
    #   if(k == 27):
    #       break

    # cv2.destroyAllWindows()

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

angles = np.array([7.5,8.5,9.5,10.5,11.5,12.5,6.5,5.5,4.5,3.5,2.5])
ptr=0
status=0
with picamera.PiCamera() as cam1:
    cam1.resolution = (200,200)
    cam1.start_preview()
    time.sleep(2)
    while True:
        s.connect((HOST, PORT))
        s.sendall('1')
        res2 = s.recv(1024)
        s.close
        if res2==1 :
            ptr=0
            c.ChangeDutyCycle(angles[ptr])
            SKIM()
            STOP()
            if status == 5
                status=0
            else
                status=3
        elif res2==2 :
            BACK()
            time.sleep(1.5)
            STOP()
        elif status == 3 : 
            BACK()
            time.sleep(1.5)
            STOP()
            status = 4
        elif status ==4 :
            FRONT()
            time.sleep(1.5)
            STOP()
            status=5
        elif status==0 :
            NOSKIM()
            c.ChangeDutyCycle(angles[ptr])
            time.sleep(0.5)
            stream = io.BytesIO()
            cam1.capture(stream , format = 'jpeg')
            res1=readImage(stream)
            if res1==1:
                status=1
                if ptr > 5 :
                    delay = ptr-5
                    BACK()
                    time.sleep(1.5)
                    LEFT()
                    time.sleep(delay)
                    FRONT()
                    ptr=0
                else :
                    delay = ptr
                    BACK()
                    time.sleep(1.5)
                    RIGHT()
                    time.sleep(delay)
                    FRONT()
                    ptr=0
            else :
                ptr+=1
            if ptr == len(angles):
                ptr=0
        else :
            status =0

    	
	