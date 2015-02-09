#name variables
sum = 0
ave = 0
grandtot = 0
grandave= 0
total= 0
#create list of numbers to average (this variable is used for the length)
numberlist=[3, 41, 12, 9, 74, 15]
#create itervar to do running average loop 
for numberlist2 in (3, 41, 12, 9, 74, 15):
	#create sum variable for grand total
	sum= sum + numberlist2
	#create average variable for running average
	ave = sum/ float (len(numberlist))
	#create overall total variable
	grandtot= total + sum
	#create overall average
	grandave= grandtot/ float (len(numberlist))
	# print 'running total: ' , (sum)
	print 'running ave: ' , (ave)

# print both overall total and overall average
print "The overall sum of the list is", (grandtot)
print "The overall average of the list is", (grandave)
	

