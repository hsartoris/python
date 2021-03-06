'''
Created on Sep 12, 2013

@author: hsartoris
'''
mondayMiles = 9.0
tuesdayMiles = 5.0
thursdayMiles = 3.1

mondayMinutes = 75
tuesdayMinutes = 40
thursdayMinutes = 21

mondaySeconds = 32
tuesdaySeconds = 53
thursdaySeconds = 9

mondayTime = (mondayMinutes * 60) + mondaySeconds
tuesdayTime = (tuesdayMinutes * 60) + tuesdaySeconds
thursdayTime = (thursdayMinutes * 60) + thursdaySeconds

totalMiles = mondayMiles + tuesdayMiles + thursdayMiles
totalTime = mondayTime + tuesdayTime + thursdayTime
totalMinutes = int(totalTime / 60)
totalSeconds = int(totalTime % 60)

mondayAverageSpeed = mondayTime / mondayMiles
mondayAverageMinutes = int(mondayAverageSpeed / 60)
mondayAverageSeconds = int(mondayAverageSpeed % 60)

tuesdayAverageSpeed = tuesdayTime / tuesdayMiles
tuesdayAverageMinutes = int(tuesdayAverageSpeed / 60)
tuesdayAverageSeconds = int(tuesdayAverageSpeed % 60)

thursdayAverageSpeed = thursdayTime / thursdayMiles
thursdayAverageMinutes = int(thursdayAverageSpeed / 60)
thursdayAverageSeconds = int(thursdayAverageSpeed % 60)

totalAverageSpeed = totalTime / totalMiles
totalAverageMinutes = int(totalAverageSpeed / 60)
totalAverageSeconds = int(totalAverageSpeed % 60)

print "Total distance run " + str(totalMiles) + " miles"
print "Total time run " + str(totalMinutes) + " minutes and " + str(totalSeconds) + " seconds"
print "Average speed on Monday is " + str(mondayAverageMinutes) + " minutes and " + str(mondayAverageSeconds) + " seconds per mile"
print "Average speed on Tuesday is " + str(tuesdayAverageMinutes) + " minutes and " + str(tuesdayAverageSeconds) + " seconds per mile"
print "Average speed on Thursday is " + str(thursdayAverageMinutes) + " minutes and " + str(thursdayAverageSeconds) + " seconds per mile"
print "Average overall speed is " + str(totalAverageMinutes) + " minutes and " + str(totalAverageSeconds) + " seconds per mile"