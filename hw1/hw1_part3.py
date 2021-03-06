'''
Created on Sep 12, 2013

@author: hsartoris
'''

def babylonian(x, y):
    return (y + (x/y)) / 2

print "Computing the sqrt of 2.0"
estimate = babylonian(2.0, 1.0)

for i in range(1,6):
    print "Estimate " + str(i) + ": " + str(estimate)
    estimate = babylonian(2.0, estimate)
    
print "Computing the sqrt of 10.0"
estimate = babylonian(10.0, 1.0)

for i in range(1,7):
    print "Estimate " + str(i) + ": " + str(estimate)
    estimate = babylonian(10.0, estimate)