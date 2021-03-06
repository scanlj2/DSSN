import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) #if RPi.GPIO detects
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) #IR LED
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP) # IR Detector - add in a 10k pull-up resistor

try:
    sensorState = 1
    while True:
        GPIO.output(11, GPIO.HIGH)
        sensorState = GPIO.input(5)
        if(sensorState == GPIO.LOW):
            print("Beam broken - Intruder alert")
	else:
	    print("everything is safe")
	time.sleep(1)
except:
    GPIO.cleanup()
