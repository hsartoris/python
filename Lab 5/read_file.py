'''
Created on Sep 23, 2013

@author: hsartoris
'''


in_file = 0

if (raw_input("Short or long file? (S/L)") == "S"):
    in_file = open("yelp-short.txt", 'r')
else:
    in_file = open("yelp.txt", 'r')

for line in in_file:
    print line, len(line)