import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio

ESC1=4
ESC2=17 
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)

max_value = 2000 
min_value = 700

print("enter speed between 700 to 2000")
while True:
    inp = raw_input()
    if inp == 0:
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
    	pi.stop()
    elif inp>=700 and inp<=2000:
        pi.set_servo_pulsewidth(ESC1,inp)
        pi.set_servo_pulsewidth(ESC2,inp)
    else:
    	break