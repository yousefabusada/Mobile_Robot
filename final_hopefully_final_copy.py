#new finally
#remove the part where the motor move forward when turning.
#orientation_Adjusment
import RPi.GPIO as GPIO
#from sys import sys.path.insert()
#sys.path.insert(0, '/Desktop/anotherSIMPLE_encoder.py') #sys.path.insert(0, '/path/to/application/app/folder')
#sys.path.insert(0, '/Desktop/ultrasonic.py')
import SpeedSensor_mod
import range_sensor as us 
import ReadCompass9150 as compass
import motors as motors
import time
import math
ss = SpeedSensor_mod.SpeedSensor_mod(21)
N				=	90 #number of slots
R				= 	5 # diameter
theta_required = 0
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(led,GPIO.OUT)
    #GPIO.setup(m11,GPIO.OUT)
    #GPIO.setup(m12,GPIO.OUT)
    #GPIO.setup(m21,GPIO.OUT)
    #GPIO.setup(m22,GPIO.OUT)
    #GPIO.output(led, 1)
    time.sleep(5)

def orientation_Adjustment():
    global theta_required
    if( us.avgDistance_front() < 20):
	    motors.stop()
	    return
    print("you're now in the function orientation adjustment")
    dis=math.sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)
    slope = abs((Y_F - Y_0)/ (X_F -X_0))
    print(" the slope is ", slope)
    theta_required= round(math.degrees(math.atan(slope)), 0)
    print("theta required=", theta_required)
    #print type(theta_required)
    angle = compass.readcompasscalibrated()
    print "angle is: " + str(type(angle))
    if(str(type(angle)) != "<type 'NoneType'>"):
		angle = round(angle, 0)
		if abs((angle-theta_required)) < abs((360 + theta_required - angle)):
			motors.right()
			print("Orie_adju>>> if..right()")
			#time.sleep(1)
		else:
			motors.left()
			print("Orie_adju>>> else..Left()")
			#time.sleep(2)
			#is the angle above == angle below? 
			#if the angle is the required angle it stops
			#then it breaks and return 0 as orien_adj value.
			#ultrasonic has no attribute here.
			#
    while True:
		print "or adjust"
		
		angle = compass.readcompasscalibrated()
		if(str(type(angle)) == "<type 'NoneType'>"):
			continue
		angle = round(angle, 0)
		print "angle is: " + str(type(angle))
		if ((angle - theta_required) <= 20 or (angle - theta_required) >= -20 ):
		#if ((angle - theta_required) == 20) or ((angle - theta_required) == -20):
			
		#if (angle -round(theta_required, 0)==20) or(angle-round(theta_required, 0)==-20):
			motors.stop()
			#time.sleep(10)
			print "Stop: angle = theta_required"
			break
		motors.forward()		
			
	
    return 0
	
    #adjust then forward
    # u have to fugure out how to fucking do it!!
    #return orientation_Adjusment
def predicting_obstacle():
    print("now we're in the predicting_obstacle function")
	
    lastAvgDistance = us.avgDistance_front() #kef nnsaweha mn el last iteration
    #Move forward 
    
    global lastAvgDistance
    if lastAvgDistance <= 30:
    #if lastAvgDistance-avgDistance<=30:
        motors.left()
        sleep(0.1)
        predicting_obstacle()

def check_for_obstacle():
	print("now we're in the check_for_obstacle function")
	distance_measured = us.avgDistance_front()
	while True:
		motors.left()
		time.sleep(0.5)
		if(us.avgDistance_front() - distance_measured) > 0:
			motors.stop()
			break
	return
if __name__=='__main__':
    setup()
    X_0=0
    Y_0=0
    r=3.5
    cir=2*math.pi*r
    slots=90 #number of slots
    #Sleep_time90=(slots/40)/(rotational_speed)*60 #if rotational_speed in rev/sec. 60 to conert it to seconds
    user_input = str(raw_input("enter final position in x y coordinates: "))
    X_F,Y_F= user_input.split(' ')
    X_F = int(X_F)
    Y_F = int(Y_F)
    #print X_F
    #print Y_F
    dis=math.sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)
    distance_in_counts = N*dis / cir
    ss.setArrival(distance_in_counts+10)
   
    print("distance in counts", distance_in_counts)
    
    while True:
		print("entered the while loop")
		#orientation_Adjustment = 
		#orientation_Adjustment() 
		if us.avgDistance_front() >= 20:
			orientation_Adjustment()
			print("average distanve>= 20")
			#motors.forward()
		#elif us.avgDistance_front()<20:
			print("average distanve < 20")
			measure_angle = compass.readcompasscalibrated()
			if (str(type(measure_angle)) != "<type 'NoneType'>"):
				X_0 += ss.getDistance() * math.cos(measure_angle- theta_required)
				Y_0 += ss.getDistance() * math.sin(measure_angle- theta_required)
				motors.stop()
				time.sleep(0.1)
				print("now we go left")
				motors.left()
				print("then check for obstacle")
				check_for_obstacle()
				ss.startTrackingDistance()
				motors.forward()
				distance_in_counts = (N * math.sqrt((Y_F-Y_0)**2 + (X_F-X_0)**2)) / cir
				ss.setArrival((distance_in_counts + 10))
