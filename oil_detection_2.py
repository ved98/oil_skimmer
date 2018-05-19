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
	       		
	print count2*100/(count1+count2)

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

img = cv2.imread(sys.argv[1], 1) # load image, 1 means load in RGB format

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
# mask2 = cv2.dilate(mask2,kernel,iterations = 1)
# mask2 = cv2.medianBlur(mask2, 5)

# contours2, hierarchy2 = cv2.findContours(mask_brick, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# idx=0
# for cnt in contours2:
#     idx += 1
#     x,y,w,h = cv2.boundingRect(cnt)
#     roi = mask_brick[y:y+h,x:x+w]
#     cv2.imwrite(str(idx) + '.jpg', roi)
#     cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)

rows = mask.shape[0]
cols = mask.shape[1]
print rows
print cols

count = detectBoundaries()
if(count/(rows*cols)*100 > 30):
	backwards()
	sleep(3)

blackPercentage()

cv2.namedWindow('oil', cv2.WINDOW_NORMAL)
cv2.resizeWindow('oil', 600, 600)
cv2.imshow('oil', mask)

cv2.namedWindow('oil_2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('oil_2', 600, 600)
cv2.imshow('oil_2', mask2)

cv2.namedWindow('brick', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('brick', 600, 600)
cv2.imshow('brick', mask_brick)

cv2.namedWindow('bgr', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('bgr', 600, 600)
cv2.imshow('bgr', img)

cv2.waitKey(0)

cv2.destroyAllWindows()