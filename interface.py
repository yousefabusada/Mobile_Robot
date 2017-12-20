import RPi.GPIO as GPIO
import Tkinter as graphics
import tkMessageBox

sensors = {}
actuators = {}
pins = {}

root = graphics.Tk().withdraw()
def setMode(mode):
		
	if(mode.upper() == "BCM"): #Check input if equal to "BCM" and set GPIO mode to "GPIO.BCM"
		GPIO.setmode(GPIO.BCM)
	elif(mode.upper() == "BOARD"): #Check input if equal to "BOARD" and set GPIO mode to "GPIO.BOARD"
		GPIO.setmode(GPIO.BOARD)
	else:	
		GPIO.setmode(GPIO.BCM) #Sets the Raspberry Pi's GPIO pins to follow the GPIO.BOARD mode pinout as a default if no appropriate mode value was entered.
		
def addSensor(name,pin):
	status = checkStatus(pin)
	
	if(status==0):
		GPIO.setup(pin, GPIO.IN)
		sensors[pin] = name
		pins[pin] = 1
	elif(status == 1): #Checks whether this pin is reserved for another sensor.
		#warnings.warn("This pin is reserved for a sensor, remove pin ")
		tkMessageBox.showwarning("Warning!","This pin is reserved for another sensor, please remove the sensor definition and then try again.")			
	elif(status == 2): #Checks whether this pin is reserved for an actuator.
		#warnings.warn("This pin is reserved for an Actuator, remove pin ")
		tkMessageBox.showwarning("Warning!","This pin is reserved for an actuator, please remove the actuator definition and then try again.")
	
def removeSensor(pin):
	if(checkStatus(pin) != 0):
		del sensors[pin]
		del pins[pin]
		GPIO.setup(pin, GPIO.OUT)

def addActuator(name,pin):
	status = checkStatus(pin)
	if(status == 0):
		GPIO.setup(pin, GPIO.OUT)
		actuators[pin] = name
		pins[pin] = 2
	elif(status == 1): #Checks whether this pin is reserved for a sensor.
		#warnings.warn("This pin is reserved for a sensor, remove pin ")
		tkMessageBox.showwarning("Warning!","This pin is reserved for a sensor, please remove the sensor definition and then try again.")			
	elif(status == 2): #Checks whether this pin is reserved for another actuator.
		#warnings.warn("This pin is reserved for an Actuator, remove pin ")
		tkMessageBox.showwarning("Warning!","This pin is reserved for another actuator, please remove the actuator definition and then try again.")
		
def removeActuator(pin):
	if(checkStatus(pin) != 0):
		del actuators[pin]
		del pins[pin]
		
def checkStatus(pin):
	if(pin in pins):
		if(pins[pin] == 1):
			return 1
		elif (pins[pin] == 2):
			return 2
	else:
		return 0
		
def readSensor(pin):
	return GPIO.input(pin)
	
def setActuatof(pin,level):
	if(level == "HIGH"):
		GPIO.output(pin, GPIO.HIGH)
	elif (level == "LOW"):
		GPIO.output(pin,GPIO.LOW)

def getGPIO():
	return GPIO
def linkInterrupt(pin,state,function):
	#GPIO.add_event_detect(pin,GPIO.RISING,callback = function.readRawSensorData)
	if(state == "GPIO.RISING"):
		v = GPIO.add_event_detect(pin,GPIO.RISING,callback = function)
		return v
	elif(state == "GPIO.FALLING"):
		return GPIO.add_event_detect(pin,GPIO.FALLING,callback = function)
		
	
	
#setMode("BOARD") #Set GPIO pinout mode to "GPIO.BOARD" mode as a default
#print "GPIO.BOARD mode has been set as a default"
