import time
import picamera
import io
import cv2
import numpy as np
 stream = io.BytesIO()
with picamera.PiCamera() as cam1:
	cam1.start_preview()
	time.sleep(2)
	cam1.capture(stream , format = 'jpeg')