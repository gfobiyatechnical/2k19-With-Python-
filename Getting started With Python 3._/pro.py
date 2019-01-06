name2 = "rakesh"
name1 = 100
list = [12, 'takeit', "rakesg", 10.3]

name = int(input("enter your age : " ))	
cu_age = int(input("your current year"))
def dob(name, cu_age):
    birth = cu_age - name
    return birth	
print( dob(name, cu_age) )
file1 = open("boss.txt","r")
display = file1.read()
print(display)
liee1.close()

file2 = open("poss2.txt","w")
file2.write("I am not your boss")
boss = file2.read()
print(boss)






