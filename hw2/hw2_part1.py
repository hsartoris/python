'''
Created on Sep 15, 2013

@author: hsartoris
'''
from array import array

radius = 3.5
offset = 2

actorX = array('i', [0,0,0,0])
actorY = array('i', [0,0,0,0])

for i in range(0,4):
    actorX[i] = int(raw_input("Enter actor " + str(i) + " x position: "))
    print str(actorX[i])
    actorY[i] = int(raw_input("Enter actor " + str(i) + " y position: "))
    print str(actorY[i])

minX = actorX[0] - (radius + offset)
minY = actorY[0] - (radius + offset)
maxX = actorX[0] + (radius + offset)
maxY = actorY[0] + (radius + offset)

for i in range(0,4):
    if (actorX[i] - (radius + offset)) < minX:
        minX = actorX[i] - (radius + offset)
    if (actorY[i] - (radius + offset)) < minY:
        minY = actorY[i] - (radius + offset)
    if (actorX[i] + (radius + offset)) > maxX:
        maxX = actorX[i] + (radius + offset)
    if (actorY[i] + (radius + offset)) > maxY:
        maxY = actorY[i] + (radius + offset)
    
print "The lower corner of the rectangle is (" + str(minX) + ", " + str(minY) + ")"
print "The upper corner of the rectangle is (" + str(maxX) + ", " + str(maxY) + ")"