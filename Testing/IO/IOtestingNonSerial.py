import time
import RPi.GPIO as GPIO

#Board Pin Mode Setup
GPIO.setmode(GPIO.BCM)

#Variable Definitions
#Components
Proximity_Sensor = 11

#Flags
Launch = 17
Skirt = 10
PowerOffin30 = 9

#IO Setup
#Flags
GPIO.setup(Launch, GPIO.IN)
GPIO.setup(Skirt, GPIO.IN)
GPIO.setup(PowerOffin30, GPIO.IN)

#Proximity Sensor
GPIO.setup(Proximity_Sensor, GPIO.IN)
	
#--------------------------------------------------------------------------
#Begin Program
#Starting Print

print('This software is for IO Testing 2019. \n')


while(true):
	print('Current Values are: Launch Signal= ')
	print(str(GPIO.input(Launch)))
	print(' |Skirt Signal= '())
	print(str(GPIO.input(Skirt)))
	print(' |PowerOffin30 Signal= ')
	print(str(GPIO.input(PowerOffin30)))
	print(' |ProximitySensor Signal= ')
	print(str(GPIO.input(Proximity_Sensor)))
	print('\n')
	time.sleep(.10)