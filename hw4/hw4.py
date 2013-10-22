'''
Created on Oct 9, 2013

@author: hsartoris
'''

census = open("census_data.txt")
data = []

for line in census:
    temp = line.strip().strip('\n').split('|')
    temp[2] = int(temp[2].replace(',', ''))
    temp[3] = int(temp[3].replace(',', ''))
    data.append(temp)
census.close()

largestCounty2010 = ["", 0]
smallestCounty2010 = ["", 99999]
totalPop = 0
largestCity2010 = ["", 0]
smallestCity2010 = ["", 999999999999]
largestTown2010 = ["", 0]
smallestTown2010 = ["", 99999]
smallestChangeCounty = ["", 1]
largestChangeCounty = ["", 0]
countyPopulations = []
numCounties = 0
counties = []
subdivide = []

for l in data:
    if l[1] == 'county':
        if l[3] > largestCounty2010[1]:
            largestCounty2010[0] = l[0]
            largestCounty2010[1] = l[3]
        if l[3] < smallestCounty2010[1]:
            smallestCounty2010[0] = l[0]
            smallestCounty2010[1] = l[3]
        
        if abs((l[3] - l[2])/float(l[2])) * 100 > abs(largestChangeCounty[1]):
            largestChangeCounty[0] = l[0]
            largestChangeCounty[1] = (l[3] - l[2])/float(l[2]) * 100
        if abs((l[3] - l[2])/float(l[2])) * 100 < abs(smallestChangeCounty[1]):
            smallestChangeCounty[0] = l[0]
            smallestChangeCounty[1] = (l[3] - l[2])/float(l[2]) * 100
        
        if l[3] not in countyPopulations:
            countyPopulations.append(l[3])
            
        totalPop += l[3]
        counties.append(l[0])
        subdivide.append([])
        numCounties += 1
    elif numCounties > 0:
        subdivide[numCounties-1].append(l)
    
    if l[1] == 'city':
        if l[3] > largestCity2010[1]:
            largestCity2010[0] = l[0]
            largestCity2010[1] = l[3]
        if l[3] < smallestCity2010[1]:
            smallestCity2010[0] = l[0]
            smallestCity2010[1] = l[3]
            
    if l[1] == 'town':
        if l[3] > largestTown2010[1]:
            largestTown2010[0] = l[0]
            largestTown2010[1] = l[3]
        if l[3] < smallestTown2010[1]:
            smallestTown2010[0] = l[0]
            smallestTown2010[1] = l[3]

averagePop = totalPop / numCounties

countyPopulations.sort()

median = 0
if len(countyPopulations) % 2 == 0:
    median = countyPopulations[len(countyPopulations)/2]
else:
    median = (countyPopulations[len(countyPopulations)/2] + countyPopulations[len(countyPopulations)/2]) / 2
    

countyStuff = []
sizes = []
for j in range(0, len(subdivide)):
    county = subdivide[j]
    countyStuff.append([False, False, False])
    sizes.append([])
    for i in range(0,len(county)):
        sizes[j].append(county[i][3])
        if county[i][1] == 'city':
            countyStuff[j][0] = True
        if county[i][1] == 'town':
            countyStuff[j][1] = True
        if county[i][1] == 'reservation':
            countyStuff[j][2] = True

countiesWithEverything = []
for i in range(0, len(countyStuff)):
    if countyStuff[i][0] and countyStuff[i][1] and countyStuff[i][2]:
        countiesWithEverything.append(counties[i])

medians = []
for array in sizes:
    array.sort()
    if len(array) % 2 == 0:
        medians.append((array[len(array) / 2] + array[(len(array) / 2) + 1]) / 2)
    else:
        medians.append(array[(len(array) / 2)])

medianLowCounty = ["", 9999999999]

for i in range(0, len(medians)):
    if medians[i] < medianLowCounty[1]:
        medianLowCounty = [counties[i], medians[i]]



print " 1. Largest county: ", largestCounty2010
print " 2. Smallest county: ", smallestCounty2010
print " 3. County population average: ", averagePop
print "    County median population: ", median
print " 4. Largest city: ", largestCity2010
print " 5. Smallest city: ", smallestCity2010
print " 6. Largest town: ", largestTown2010
print " 7. Smallest town: ", smallestTown2010
print " 8. Largest percent change: ", largestChangeCounty
print " 9. Smallest percent change: ", smallestChangeCounty
print "10. Counties with all subtypes: ", countiesWithEverything
print "11. Smallest median county size: ", medianLowCounty