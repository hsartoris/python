'''
Created on Sep 23, 2013

@author: hsartoris
'''

def parseLine(pLine):
    pLine = pLine.strip('\n')
    pLine = pLine.split('|')
    ratings = []
    ratingsTotal = 0
    if len(pLine) > 6:
        for i in range(6, len(pLine)):
            ratingsTotal += int(pLine[i])
            ratings.append(int(pLine[i]))
    ratingsTotal /= float(len(pLine) - 6)
    return [pLine[0], float(pLine[1]), float(pLine[2]), pLine[5], ratings, ratingsTotal]
    

in_file = 0

if (raw_input("Short or long file? (S/L)") == "S"):
    in_file = open("yelp-short.txt", 'r')
else:
    in_file = open("yelp.txt", 'r')

rType = raw_input("Enter your restaurant type preference: ")
rating = float(raw_input("Enter you minimum average review score: "))

totalRestaurants = 0
for line in in_file:
    p_line = parseLine(line)
    if p_line[3] == rType and p_line[len(p_line) - 1] >= rating :
        print "Name: " + p_line[0] + ";  Rating: " + str(round(p_line[len(p_line) - 1], 2))
        totalRestaurants += 1
print "Found " + str(totalRestaurants) + " restaurants."