List = [1,2,3,4,5,5,5,2,1,6]
pappu=set()
nalla=[]
for i in List:
	if i not in pappu:
		nalla.append(i)
		pappu.add(i)

print(nalla)		
