'''
Created on Sep 23, 2013

@author: hsartoris
'''
def parseLine(pLine):
    pLine = pLine.strip('\n')
    pLine = pLine.split('|')
    ratings = []
    if len(pLine) > 6:
        for i in range(6, len(pLine)):
            ratings.append(pLine[i])
    return [pLine[0], pLine[1], pLine[2], pLine[5], ratings]
    

in_file = 0

if (raw_input("Short or long file? (S/L)") == "S"):
    in_file = open("yelp-short.txt", 'r')
else:
    in_file = open("yelp.txt", 'r')


for line in in_file:
    p_line = parseLine(line)
    print p_line