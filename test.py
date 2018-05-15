import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo = 3
GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)
front =7.5
left=5
right=10
p.start(front)

try:
        while True:
        #time.sleep(2)
		p.ChangeDutyCycle(left)  # turn towards 90 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(right)  # turn towards 0 degree
		time.sleep(1) # sleep 1 second
##		p.ChangeDutyCycle(12.5) # turn towards 180 degree
##                time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
