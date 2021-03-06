'''
Created on Sep 12, 2013

@author: hsartoris
'''

def percentInc(x,y):
    return ((x - y) / x) * -100

ns2006 = 62130.
ns2008 = 66310.
ns2010 = 69160.
ns2012 = 72560.

rs2006 = 93950.
rs2008 = 97970.
rs2010 = 100660.
rs2012 = 102190.

pns2008 = percentInc(ns2006, ns2008)
pns2010 = percentInc(ns2008, ns2010)
pns2012 = percentInc(ns2010, ns2012)

prs2008 = percentInc(rs2006, rs2008)
prs2010 = percentInc(rs2008, rs2010)
prs2012 = percentInc(rs2010, rs2012)

r2006 = rs2006/ns2006
r2008 = rs2008/ns2008
r2010 = rs2010/ns2010
r2012 = rs2012/ns2012

minimum = 50.
maximum = 0.

if (r2006 > maximum):
    maximum = r2006
if (r2008 > maximum):
    maximum = r2008
if (r2010 > maximum):
    maximum = r2010
if (r2012 > maximum):
    maximum = r2012

if (r2006 < minimum):
    minimum = r2006
if (r2008 < minimum):
    minimum = r2008
if (r2010 < minimum):
    minimum = r2010
if (r2012 < minimum):
    minimum = r2012
    
print "Percent increase 2006 to 2008 for network and systems is " + str(pns2008)
print "Percent increase 2006 to 2008 for research scientists is " + str(prs2008)
print "Percent increase 2008 to 2010 for network and systems is " + str(pns2010)
print "Percent increase 2008 to 2010 for research scientists is " + str(prs2010)
print "Percent increase 2010 to 2012 for network and systems is " + str(pns2012)
print "Percent increase 2010 to 2012 for research scientists is " + str(prs2012)
print ""
print "Min ratio of salaries across four different years is " + str(minimum)
print "Max ratio of salaries across four different years is " + str(maximum)