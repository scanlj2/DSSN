# This code will test the pan/tilt camera module.

# Imports for taking a picture
import datetime
from time import sleep
from picamera import PiCamera

# Imports for panning/tilting
from adafruit_servokit import ServoKit

# Create the camera object
camera = PiCamera()

# Create the servo object
kit = ServoKit(channels=16)
# 0 is pan, 1 is tilt

# Set ranges
kit.servo[0].actuation_range = 180 # Default
kit.servo[1].actuation_range = 360 #150

counter = 0

while True:

    # Pan left on even counts and right on odd counts
    if counter%2 == 0:
        # Pan left
        print('Panning left')
        kit.servo[0].angle =75
    #elif counter%2 == 1:
        # Pan right
       # print('Panning right')
        #kit.servo[0].angle = 100
    #elif counter%2 == 2:
	# Pan down
        #print('Panning up')
        #kit.servo[1].angle = 0
    #else:
        # Pan up
        #print('Panning down')
        #kit.servo[1].angle = 360

    counter = counter + 1
    
    # Get the camera ready
    camera.start_preview()
    
    # Camera warm up time
    sleep(2) 
    
    # Get the date to name the file
    date = datetime.datetime.now()
    date_string = date.strftime("%m_%d_%Y_%H_%M_%S")
    
    # Take the picture
    #camera.capture('/home/pi/Documents/DSSN/Project/Pictures/' + date_string + '.jpg')
    print('Done taking picture')
