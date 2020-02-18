#Rocksat X Payload Code for testing 2019 Stepper
#UPRRP Team
#Coded by: John G. Wilson Negroni
#jgwilson1997@gmail.com
#---------------------------------------------

#Imports
import RPi.GPIO as GPIO
from Stepper import Stepper

#Board Pin Mode Setup
GPIO.setmode(GPIO.BCM)

#Variable Definitions
#Stepper Motor
Step_Ena = 22
Step_Dir = 24
Step_Step = 5

step_amount = 100000 #Change this for amount of steps to test with.

#IO Setup
#Stepper Motor
GPIO.setup(Step_Ena, GPIO.OUT)
GPIO.setup(Step_Dir, GPIO.OUT)
GPIO.setup(Step_Step, GPIO.OUT)

#Stepper Setup
DoorStepper = Stepper([Step_Step,Step_Dir,Step_Ena])

#Function Definitions
#Move Motor
def MoveMotor(direction, steps):
	DoorStepper.step(steps, dir = direction)
	
#--------------------------------------------------------------------------
#Begin Program
#Starting Print
print("Rocksat X 2019 Stepper Motor Testing.")

#Move Right
print("Moving Right with 100000 steps.")
MoveMotor("right", step_amount)

#Move Left
print("Moving Left with 100000 steps.")
MoveMotor("left", step_amount)
