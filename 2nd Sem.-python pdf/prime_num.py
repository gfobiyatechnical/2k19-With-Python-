# author: Rakesh yadav
# aim: Extract the elements of a string that are positioned on prime indices

l = list(input("enter string value: "))
str_len = len(l)
m=[]
for num in range(2,str_len):
  if num%2==0 & 2!=num:
    continue    
  else:
    m.append(l[num])
print(m)    
    
