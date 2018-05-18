import RPi.GPIO as GPIO
import pigpio
pi = pigpio.pi();
pi.set_servo_pulsewidth(21,1250)


