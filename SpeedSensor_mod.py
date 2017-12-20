import interface as interface
import time as time
import math

startTime = time.time()
speedCounter 	= 	0
DistanceCounter = 	0
trackDistance	=	0
speed 			=	0
elapsed 		= 	startTime
N				=	90 #number of slots
R				= 	5 # diameter
cir				= 	2*math.pi*R
total_dis		=	0
class SpeedSensor_mod(object):


	def __init__(self,pin):
		interface.setMode("BCM")
		interface.addSensor("Photo Counter Speed Sensor",pin)
		interface.linkInterrupt(pin,"GPIO.RISING",self.calculateSpeed)
		self.pin = pin
	def calculateSpeed(self,channel):
		global speedCounter
		global startTime
		global speed
		global elapsed
		global DistanceCounter
		speedCounter = speedCounter+1
		DistanceCounter += 1
		elapsed = time.time()-startTime
		checkArrival()
		"""if(elapsed >= 1.0):
			startTime = time.time()

			speedCounter = 0
			"""
	def getLastSpeed(self):
		global speedCounter
		global elapsed
		global speed
		while True:
			if (elapsed >= 1.0):

				#Distance()
				speed = ((speedCounter/(elapsed* N))*1) #20 is num of slots
				speedCounter = 0
				startTime = time.time()
				break

		#speedCounter = 0
		#startTime = 0
		return speed
			#print speed
		#speedCounter = 0
		#print speedCounter
		#return speed
	def startTrackingDistance(self):
		global trackDistance
		trackDistance = DistanceCounter
	def getDistance(self):
		global distnaceCount
		distance = (DistanceCounter - trackDistance) * (cir / N)
		return distance
		
	def checkArrival():
		global arrival
		global DistanceCounter
		if arrival == DistanceCounter:
			stop()
	
	def setArrival(self, value):
		global arrival
		arrival = value + DistanceCounter

	'''def readRawSensorData(self,channel):

		val = interface.readSensor(self.pin)
		print val
	'''
		#return val
	"""def readSpeed():
		global startTime
		global speedCounter++
		timeNow = time.time()
		if(timeNow - startTime >= 1):
			speed = (speedCounter*1.0)/(timeNow-startTime)
			speedCounter = 0
			startTime = time.time()
			return speed
		"""
