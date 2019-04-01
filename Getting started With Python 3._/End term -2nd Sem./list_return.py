def mul_(l):
	Sum = sum(l)
	mult=1
	for i in l:
		mult = mult*i
	return (Sum,mult)

List=[1,2,3,4,5]
x = mul_(List)
print (x)
