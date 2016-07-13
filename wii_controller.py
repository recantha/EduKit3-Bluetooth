# CamJam EduKit 3 - Robotics
# Wii controller remote control script

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import os

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Left():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Right():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

StopMotors()

# Credit for this part must go to:
# Author : Matt Hawkins (adapted by Michael Horne)
# http://www.raspberrypi-spy.co.uk/?p=1101
# -----------------------
# Import required Python libraries
# -----------------------
import cwiid

PIN_LED = 25
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, 0)

button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
GPIO.output(PIN_LED, 1)
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    wii=cwiid.Wiimote()
    GPIO.output(PIN_LED, 0)

except RuntimeError:
    print "Error opening wiimote connection"
    GPIO.output(PIN_LED, 0)
    # Uncomment this line to shutdown the Pi if pairing fails
    #os.system("sudo halt")
    quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

for x in range(0,3):
    GPIO.output(PIN_LED, 1)
    time.sleep(0.25)
    GPIO.output(PIN_LED, 0)
    time.sleep(0.25)

wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    # If Plus and Minus buttons pressed
    # together then rumble and quit.
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
        print '\nClosing connection ...'
        wii.rumble = 1
        GPIO.output(PIN_LED, 1)
        time.sleep(1)
        wii.rumble = 0
        GPIO.output(PIN_LED, 0)
        os.system("sudo halt")
        exit(wii)
  
    # Check if other buttons are pressed by
    # doing a bitwise AND of the buttons number
    # and the predefined constant for that button.
    if (buttons & cwiid.BTN_LEFT):
        print 'Left pressed'
        Left()
        time.sleep(button_delay)         

    elif(buttons & cwiid.BTN_RIGHT):
        print 'Right pressed'
        Right()
        time.sleep(button_delay)          

    elif (buttons & cwiid.BTN_UP):
        print 'Up pressed' 
        Forwards()       
        time.sleep(button_delay)          
    
    elif (buttons & cwiid.BTN_DOWN):
        print 'Down pressed'      
        Backwards()
        time.sleep(button_delay)  
    
    else:
        StopMotors()
