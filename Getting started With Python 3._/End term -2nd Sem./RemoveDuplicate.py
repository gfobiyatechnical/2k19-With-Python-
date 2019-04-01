def RemoveDuplicate(l):
	for k in range(len(l)):
		l.sort()
		m = l.count(k)
		if m > 1:
			for i in range(1,m):
				n = l.index(k)
				l.pop(n)
	print(l)
			
List = [1,2,3,4,5,5,5,2,1,6]
RemoveDuplicate(List)
