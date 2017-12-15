#new finally
#remove the part where the motor move forward when turning.
#orientation_Adjusment
import RPi.GPIO as GPIO
from sys import sys.path.insert()
#sys.path.insert(0, '/Desktop/anotherSIMPLE_encoder.py') #sys.path.insert(0, '/path/to/application/app/folder')
#sys.path.insert(0, '/Desktop/ultrasonic.py')

import speedSensor.py # it has a different name on the Pi
import ultrasonic_WORK as us #again, the same thing
import time
import math
N				=	90 #number of slots
R				= 	5 # diameter
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(m11,GPIO.OUT)
    GPIO.setup(m12,GPIO.OUT)
    GPIO.setup(m21,GPIO.OUT)
    GPIO.setup(m22,GPIO.OUT)
    GPIO.output(led, 1)
    time.sleep(5)
def stop():
    print ("stop")
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("Forward")
def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print ("back")
def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("left")
def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print ("right")

def orientation_Adjustment():
    dis=sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)
    slope= (Y_F - Y_0)/ (X_F -X_0)
    print(" the slope is ", slope)
    theta_required= atan(slope)
    print("the angle of travers =", theta)
    angle = compass.readcompasscalibrated()
    if abs(angle - theta_requried) < abs(360 + theta_required - angle):
		right()
	else:
		left()
		
    while True:
		angle = compass.readcompasscalibrated()
		if angle == round(theta_required, 0):
			stop()
			break
	
	return 0
	
    #adjust then forward
    # u have to fugure out how to fucking do it!!
    return orientation_Adjusment
def predicting_obstacle():
    lastAvgDistance = us.avgDistance_front() #kef nnsaweha mn el last iteration
    #Move forward 
    
    global lastAvgDistance
	if lastAvgDistance <= 30:
    #if lastAvgDistance-avgDistance<=30:
        left()
        sleep(0.1)
        predicting_obstacle()

def check_for_obstacle():
	distance_measured = us.avgDistance_front()
	while True:
		if(us.avgDistace_front() - distance_measured) > 0:
			stop()
			break
	return
if __name__='__main__':
    setup()
    X_0=0
    Y_0=0
    r=3.5
    cir=2*pi*r
    slots=90 #number of slots
    Sleep_time90=(slots/40)/(rotational_speed)*60 #if rotational_speed in rev/sec. 60 to conert it to seconds
    X_F, Y_F= float(input("enter final position in x y coordinates").split())
    distance_in_counts = (N * dis=sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)) / cir
    ss.setArrival(distance_in_counts + 10)
    while True:
        orientation_Adjustment = orientation_Adjustment() #Orient Robot to required angle
        if us.avgDistance_front() >= 20:
			forward()
			
        elif avgDistance_front<20:
			X_0 += ss.getDistance() * math.cos(compass.readcompasscalibrated()- theta_required)
			Y_0 += ss.getDistance() * math.sin(compass.readcompasscalibrated()- theta_required)
            stop()
            sleep(0.1)
            left()
            check_for_obstacle()
            ss.startTrackingDistance()
            forward()
            distance_in_counts = (N * dis=sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)) / cir
			ss.setArrival(distance_in_counts + 10)
