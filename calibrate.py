import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio

ESC=4  #Connect the ESC in this GPIO pin 
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000 
min_value = 700

print("Disconnect the battery and press Enter")
inp = raw_input()
if inp == '':
    pi.set_servo_pulsewidth(ESC, max_value)
    print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
    inp = raw_input()
    if inp == '':            
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(12)
        pi.set_servo_pulsewidth(ESC, 0)
        time.sleep(2)
        pi.set_servo_pulsewidth(ESC, min_value)
        time.sleep(1)
print("Calibrated")