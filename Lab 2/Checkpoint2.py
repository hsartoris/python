'''
Created on Sep 2, 2013

@author: hsartoris
'''

import math

jupiterDist = 483632000.0
earthDist = 92957100.0
jupiterDiam = 88846.0
earthDiam = 7926.0
speedOfLight = 186000

ratioDist = jupiterDist / earthDist

print "Ratio of Distance: " + str(ratioDist) + " Jupiter/Earth"

jupiterVolume = (4.0/3) * math.pi * (int(jupiterDiam/2) ^ 3)
earthVolume = (4.0/3) * math.pi * (int(earthDiam/2) ^ 3)

ratioVolume = jupiterVolume/earthVolume

print "Ratio of Volume: " + repr(ratioVolume) + " Jupiter/Earth"

jupiterTime = jupiterDist / speedOfLight
earthTime = earthDist / speedOfLight

jupiterMinutes = int(jupiterTime / 60)
jupiterSeconds = int(jupiterTime - (jupiterMinutes * 60))
earthMinutes = int(earthTime / 60)
earthSeconds = int(earthTime - (earthMinutes * 60))

print "Time to Earth: " + repr(earthMinutes) + "m " + repr(earthSeconds) + "s"
print "Time to Jupiter: " + repr(jupiterMinutes) + "m " + repr(jupiterSeconds) + "s"


