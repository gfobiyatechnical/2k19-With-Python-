'''
Author: Rakesh yadav
Tasks : write a programe in pyhton which
	1. take an input from user as string
	2. check if it is a " herrogram " string or not
	3. print ' Hetrogram '  if it is , otherwise print ' Not Hertogram '
'''

STR = input()
STR = STR.lower() 			#to convert string into lower-case.
n=0
for n in range(len(STR)):		
	m = STR.count(S[n])		#method to check no. of times that value in input string
	if m<2:
		c=1
	elif m>1:
		c=2
		break			
if c==2:
	print("Not Hertogram")
else:
	print("Hetrogram")

