import socket
import picamera
import io
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import cv2
import sys
import numpy as np

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
    count = 0
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
                count += 1
    return count


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
    #mask = skimage.measure.block_reduce(mask, (5, 5), np.max)
    rows = mask.shape[0]
    cols = mask.shape[1]
    print rows
    print cols
    count = detectBoundaries()
    if(count/(rows*cols)*100 > 15):
        return 2
    res = blackPercentage()
    if res > 30 :
        return 1
     else 
        return 0   
    # cv2.imwrite(str(inm)+"test_mask.jpg", mask)
    # inm+=1
    


HOST = '10.7.9.9'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
with picamera.PiCamera() as cam1:
    cam1.resolution = (200,200)
    cam1.start_preview()
    time.sleep(2)
    while 1:
    data = conn.recv(1024)
    if data == '1':
        print(data)
        stream = io.BytesIO()
        cam1.capture(stream , format = 'jpeg')
        res2=readImage(stream)
        conn.sendall(res2)
conn.close()

