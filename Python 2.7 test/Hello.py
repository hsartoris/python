'''
Created on Aug 26, 2013

@author: hsartoris
'''
import math

print "I'll repeat after you, unless you say stop."
while (1):
    user_string = raw_input()
    if (user_string == 'stop' or user_string == 'Stop'):
        break
    print user_string
print 'Alright, I stopped.'


pi = math.pi
volume = 4./3 * pi * 3959 ** 3
print volume
