import cv2
import sys
import numpy as np
#import os
#import skimage.measure
#name=os.listdir("data")
#for i in range(len(name)):
img = cv2.imread("data/"+sys.argv[1], 1) # load image, 1 means load in RGB format
# img = cv2.imread('abc.jpg')
##a = np.double(img)
##b = a 
##img = np.uint8(b)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to hsv
# h, s, v = cv2.split(hsv)
# v+=2
# hsv = cv2.merge((h, s, v))
cv2.imwrite("data/" + sys.argv[1] + "img.jpg", img)

lower_range = np.array([0, 0, 150], dtype=np.uint8) #lower bound of color to detect
upper_range = np.array([255, 70, 255], dtype=np.uint8) #upper bound of color to detect

#create a mask for the image
mask = cv2.inRange(hsv, lower_range, upper_range)
kernel = np.ones((7,7),np.uint8)
mask = cv2.dilate(mask,kernel,iterations = 2)
mask = cv2.medianBlur(mask, 15)
#mask = skimage.measure.block_reduce(mask, (5, 5), np.max)
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

# cv2.imshow('mask',mask)
cv2.imwrite("data/"+sys.argv[1]+"mask.jpg", mask)
# cv2.imshow('image', img)

# while(1):
# 	k = cv2.waitKey(0)
# 	if(k == 27):
# 		break

# cv2.destroyAllWindows()
