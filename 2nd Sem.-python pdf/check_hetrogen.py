S=input()
S=S.lower()
S[0]="h"

n=0
for n in range(len(S)):	
	
	m=S.count(S[n])
	if m<2:
		c=1
	elif m>1:
		c=2
		break		

	
if c==2:
	print("not hertogram")
else:
	print("hetrogram")

