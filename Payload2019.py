#Rocksat X Payload Code for August 2019 Flight
#UPRRP Team
#Coded by: John G. Wilson Negroni
#jgwilson1997@gmail.com
#---------------------------------------------

#Imports
import time
import math
import RPi.GPIO as GPIO
from Stepper import Stepper

#Board Pin Mode Setupdgithu

GPIO.setmode(GPIO.BCM)

#Variable Definitions
#Components
Proximity_Sensor = 11
UV = 25

#Stepper Motor
Step_Ena = 22
Step_Dir = 24
Step_Step = 5

#Flags
Launch = 17
Skirt = 10
PowerOffin30 = 9

#Misc
time_to_launch = 20 #225 full sequence(-16 is the marging between actual time and boot up) IE 240 is 225

Count = 0
check = 1

#IO Setup
#Stepper Motor
GPIO.setup(Step_Ena, GPIO.OUT)
GPIO.setup(Step_Dir, GPIO.OUT)
GPIO.setup(Step_Step, GPIO.OUT)

#Flags
GPIO.setup(Launch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Skirt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PowerOffin30, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Proximity Sensor
GPIO.setup(Proximity_Sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#UV
GPIO.setup(UV, GPIO.OUT)

#Stepper Setup

DoorStepper = Stepper([Step_Ena,Step_Dir,Step_Step])

#Function Definitions
#Flag Check

def FlagCheck(flag):

	InputToCheck = 1
	PrintOut = ''
	check = 1
	Count = 0
		
	if (flag == 17):
		InputToCheck = 1
		PrintOut = 'Time to Launch T(sec)= '
	if (flag == 10):
		InputToCheck = 1
		PrintOut = 'Flying Time T(sec)= '
	if (flag == 11):
		InputToCheck = 0
		PrintOut = 'Skirt is not off at T(sec)= '
	if (flag == 9):
		InputToCheck = 1
		PrintOut = 'Door still open at T(sec)= '
	while(check):
		for x in range(0,13):
			if(GPIO.input(flag) == InputToCheck):
				Count += 1
		if (Count > 10):
			check = 0       
		else:
			check = 1
			print(PrintOut)
			GetTime()
		Count = 0
	
#Open Door
def OpenDoor():
	
	#Open Door
	DoorStepper.step(288000, dir = 'right') #right == open

	print('Door Opened at T(sec)= ')
	GetTime()
	
#Close Door
def CloseDoor():
	#Close Door
	DoorStepper.step(288000, dir = 'left') #left == close 

	print('Door Closed at T(sec)= ')
	GetTime()
	
#Get Time
def truncate(number, digits) -> float:
	a = pow(10.0, digits)
	return math.trunc(a * number) / a
        
def GetTime():
	current_time = time.perf_counter() - time_to_launch
	current_time = truncate(current_time, 2)
	print(str(current_time))
	time.sleep(.20)
	
#--------------------------------------------------------------------------
#Begin Program
#Starting Print

print('Software RockSat X 2019 Revision 6/06/19 \n')
print('This software is for August Flight \n')
print('UPR Payload Alive T(sec)= ')
GetTime()

#Activate UV

GPIO.output(UV, GPIO.HIGH)
print('UV are on at T(sec)= ')
GetTime()

#Launch Flag Wait
FlagCheck(Launch)

#Rocket Launched
print('Launch T(sec)= ')
GetTime()

#Skirt Flag Wait
FlagCheck(Skirt)

#Wait for Skirt Clear 
FlagCheck(Proximity_Sensor)

#Skirt Off
print('Skirt Off T(sec)= ')
GetTime()

#Deactivate Plasma and UV
GPIO.output(UV, GPIO.LOW)

print('UV are off at T(sec)= ')
GetTime()

while (time.perf_counter() < (197 + time_to_launch)):
	print('Waiting to Deploy at T(sec)= ')
	GetTime()

#Door Open

print('Door Opening Started at T(sec)= ')
GetTime()

#Door Opening

OpenDoor()

#30 Seconds before Power Off Flag Wait

FlagCheck(PowerOffin30)

#Door Closing
	
print('Door Closing T(sec)= ')
GetTime()

CloseDoor()

#Door Closed

#Sequence End

print('Going back Home T(sec)= ')
GetTime()
