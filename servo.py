import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 50)

p.start(7.5)

try:
        while True:
                time.sleep(2)
		p.ChangeDutyCycle(5)  # turn towards 90 degree
		time.sleep(2) # sleep 1 second
		p.ChangeDutyCycle(10)  # turn towards 0 degree
##		time.sleep(5) # sleep 1 second
##		p.ChangeDutyCycle(12.5) # turn towards 180 degree
##                time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()