'''
Author: Rakesh Yadav
Aim: Return multiple values 
	1. make a funtion
	2. sum all elements of list
	3. calulate multiplication of each elements
	4. finally return sum and multiple
'''

def mul_(l):
	Sum = sum(l)
	mult=1
	for i in l:
		mult = mult*i
	return (Sum,mult)

List=[1,2,3,4,5]
x = mul_(List)
print (x)
