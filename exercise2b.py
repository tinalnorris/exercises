
sum = 0
ave = 0
grandtot = 0
grandave= 0
total= 0
l=[3, 41, 12, 9, 74, 15]
for itervar in (3, 41, 12, 9, 74, 15):
	sum= sum + itervar
	ave = sum/ float (len(l))
	grandtot= total + sum
	grandave= grandtot/ float (len(l))
	# print 'running total: ' , (sum)
	print 'running ave: ' , (ave)

print 'overall total: ' , (grandtot)
print 'overall average: ' , (grandave)
	

# n= (15, 18, 2, 36, 12, 78, 5, 6, 9)
# total = sum (n)
# average =sum (n)/float(len(n))
	
# print ("The sum of the list is", total,"and", 
# 	"the average of the list is", average)
