import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio

ESC1=17
ESC2=18
ESC3=22
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)

max_value = 2000 
min_value = 835

print("Disconnect the battery and press Enter")
inp = raw_input()
if inp == '':
    pi.set_servo_pulsewidth(ESC1, max_value)
    pi.set_servo_pulsewidth(ESC2, max_value)
    pi.set_servo_pulsewidth(ESC3, max_value)
    print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
    inp = raw_input()
    if inp == '':            
        pi.set_servo_pulsewidth(ESC1, min_value)
        pi.set_servo_pulsewidth(ESC2, min_value)
        pi.set_servo_pulsewidth(ESC3, 1100)
        time.sleep(12)
        pi.set_servo_pulsewidth(ESC1, 0)
        pi.set_servo_pulsewidth(ESC2, 0)
        pi.set_servo_pulsewidth(ESC3, 0)
        time.sleep(2)
        pi.set_servo_pulsewidth(ESC1, min_value)
        pi.set_servo_pulsewidth(ESC2, min_value)
        pi.set_servo_pulsewidth(ESC3, 1100)
        time.sleep(1)
print("Calibrated")