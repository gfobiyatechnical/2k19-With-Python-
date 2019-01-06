#Aim : Use of different functions
#Author : Rakesh Yadav

print("\tUSE oF Continue in Python:    ")
list = 'Rakesh yadav Dil SHIV Rahul'
print(list,sep="\t\t")
for x in list :
    if x == " " :
        continue
    print("\tLETTER IS %c" %x)


print("\n\tUSE OF BREAK inPython :    ")
list = 'Rakesh yadav Dil SHIV Rahul'
print(list,sep="\t\t")
for x in list :
    if x == " " :
        break
    print("\tLETTER IS %c" %x)


print("\n\tUSE OF NESTED-WHILE LOOP inPython :    ")
count = 10
x = 0
print("Count = %d" %count ,"X = %d" %x)
while x < count:
    y = 0
    
    while y < 11:
        y = y + 1
        
x  = x  + 1

