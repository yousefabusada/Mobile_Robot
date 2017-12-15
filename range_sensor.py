import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#print "Waiting For Sensor To Settle"
time.sleep(5)

def avgDistance_front(self):
	avg_distance = 0.0
	#Sum 5 distance readings
	for n in range(5):
		avg_distance += getdistance(self)
		
	return round(avg_distance/5.0, 2)
	
def getdistance(self):
	global TRIG
	global ECHO 
	while True:
		#Trigger a PULSE
		GPIO.output(TRIG, GPIO.LOW)
		time.sleep(0.06)
		GPIO.output(TRIG, GPIO.HIGH)
		time.sleep(0.06)
		GPIO.output(TRIG, GPIO.LOW)
		
		#Check for status of echo signal from ultrasonic sensor and record time.
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()
			
		#Measure time difference between the last time the signal was sent, and recieved.
		pulse_duration = pulse_end - pulse_start
		
		#Convert time difference value to distance in cm.
		distance = pulse_duration * 17150
		distance = round(distance, 2)
	
		return distance
		
		#Not needed for now, checks if there is an obstacle, implemented somewhere else. 
		'''
		if(distance <= 20.0):
			print "Obstacle, have to avoid!"
		else:
			print "path is clear!"
		'''
GPIO.cleanup()
