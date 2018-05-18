import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
#os.system ("sudo pigpiod") #Launching GPIO library
#time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio

ESC1=17
ESC2=18
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)

max_value = 2000 
min_value = 700

print("enter speed between 700 to 2000")
while True:
    inp = raw_input()
    pi.set_servo_pulsewidth(ESC1,inp)
    pi.set_servo_pulsewidth(ESC2,inp)
