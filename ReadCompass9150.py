#!/usr/bin/env python
# coding: latin-1

# Load the MPU-9150 library
import sys
import time
import decimal
import math
from MPU9150 import *

# Tell the library to disable diagnostic printouts
printFunction = NoPrint

# Start the MPU9150 module (sets up devices)
Init()
print( "before if statement")
if len(sys.argv) >= 3 and sys.argv[1].find("-n") == 0:
    n = decimal.Decimal(sys.argv[2])
    dlay = 0
    if len(sys.argv) >= 4:
        dlay = decimal.Decimal(sys.argv[3])
    print("Taking %d samples delay %d mS" % (n, dlay))
    fdlay = 0.0
    fdlay = dlay / 1000
    i = 0
    samples = []
    while n > 0:
        (mX, mY, mZ) = ReadCompassRaw()
	print("%+06d, %+06d, %+06d" % (mX, mY, mZ))
	#print("mX = %+06d, mY = %+06d, mZ = %+06d" % (mX, mY, mZ))
	samples = samples + [[mX, mY, mZ]]
	i = i + 1
	n = n - 1
	time.sleep(fdlay)
    MX = MY = MZ = MX2 = MY2 = MZ2 = 0.0
    for (mX, mY, mZ) in samples:
        MX = MX + mX
	MY = MY + mY
	MZ = MZ + mZ
    MXAve = MX / i
    MYAve = MY / i
    MZAve = MZ / i
    for (mX, mY, mZ) in samples:# tabbed
		
		MX2 = MX2 + (mX - MXAve) ** 2
		MY2 = MY2 + (mY - MYAve) ** 2
		MZ2 = MZ2 + (mZ - MZAve) ** 2
		print( "just before the readcompasscalibrated")
		print("    Avg   StdDev")
		print("mX %6.1f %3.1f" % (MX / i, math.sqrt(MX2 / i)))
		print("mY %6.1f %3.1f" % (MY / i, math.sqrt(MY2 / i)))
		print("mZ %6.1f %3.1f" % (MZ / i, math.sqrt(MZ2 / i)))
    

def readcompasscalibrated():
	#print("in da fuckn")
    #Read and display the raw magnetometer readings
    print 'mX = %+06d, mY = %+06d, mZ = %+06d' % ReadCompassRaw()
    x_reading = ReadCompassRaw()[0]
    y_reading = ReadCompassRaw()[1]
    z_reading = ReadCompassRaw()[2]
    #for i in range(5):
	#	x_reading += ReadCompassRaw()[0]
	#	y_reading += ReadCompassRaw()[1]
		#z_reading += ReadCompassRaw()[2]
	
    #x_reading = x_reading / 5.0
    #y_reading = y_reading / 5.0
    if(x_reading !=0 and y_reading != 0):
		angle = math.degrees(math.atan2(y_reading, x_reading))
		if(angle < 0):
			angle = 360 + angle
			return angle
		else:
			return angle
    elif (x_reading == 0 and y_reading > 0):
		return float(0)
    elif (x_reading == 0 and y_reading < 0):
		return float(90)
