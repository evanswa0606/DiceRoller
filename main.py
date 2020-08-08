from random import randint
import time

def total_inlist(inputlist):
	total = 0
	for i in inputlist:
		total+=i
	return total

values = [0,0,0,0,0,0]

timestoroll=int(input("How many dice to roll? "))
starttime=time.time()
while timestoroll:
	values[randint(0,5)]+=1
	timestoroll-=1
endtime=time.time()-starttime
for i in range(len(values)):
	print(f'{i}:')
	print(f'	Rolls: {values[i]}')
	print('	Percentage: %.3f%%' % (values[i]/total_inlist(values)))
print("\nTime elapsed: %.6f seconds" % (endtime))
