import time
import picamera
import io
import cv2
import numpy as np
import picamera
with picamera.PiCamera() as cam1:
    cam1.resolution = (200,200)
    cam1.start_preview()
    time.sleep(2)
    i=0
    while True:
        cam1.capture("wall/"+str(i)+".jpg")
        i+=1
       