#Point to Notice OUPUTS

print("fun - Outputs:"'\n')


print('\n')
print("As Student: You are My first love.\n\t    We will be together forever.\nAs Programmer: You are My first love But..\n\t      Lets do BREAKUP before anyone of us brokes anyone Heart.")

print('\n')
print("Mark Lassoff, 42")
print("Mark Lassoff",42)

print('\n')
print("College","Nota","Branch","Chuluu","Spesalization","Dot",sep="\t")

print('\n')
print("College","Nota","Branch","Chuluu","Spesalization","Dot",sep=" $$ ")

print('\n')
print("My name is %s and age is %d " %("Mark",42))

print("\n")
funlist = ["Nota", "Chai-pilo", "2-cups", "my number is 00", "0420"]
print("FunList:")
for item in funlist:
    print(item,sep="\n")


print("************************************************************************")
print("\n LETS HAVE SOME MATHS PRACTIC     : \n")
print("12 + 12  =    ",12+12)
print("12 * 2   =    ",12 * 2 )
print("12 ** 2  =    ",12 ** 2)
print("12 // 4  =    ",12 // 4 )
print("12 / 2   =    ",12 / 2)
print("12 - 8   =    ",12 - 8)
print("-12 - 23 =   ",-12 - 23)
print("12 - 21  =    ",12 - 21)
print("12 % 5   =    ",12 % 5)
print("12.4 * 2 =   ",12.4 * 2)
print("2 ^ 3    =   ",2 ^ 3)
print("3 ^ 2    =   ",3 ^ 2)
print("5 | 3    =   ",5 | 3)
print("2 & 5    =   ",2 & 5)
print("5 << 2   =   ",5 << 2)
print("5 >> 2   =   ",5 >> 2)
print(" ~(5)    =   ",~(5) ) #UNIRARY OPERATOR
print ("3 ** 3 * 5  =   ",3 ** 3 * 5)
print ("3 ** (3 * 5)    =   ",3** (3 * 5))
print("****************************************************************************")
print("\n")
print("\t LETS KNOW ABOUT RELATIONAL OPERATORS \t:\n")
a = 3
b = 3
print("a = ",a, "\t" ,"b = ",b )
print("a == b   =   ", a == b )
print("\n")
b = 5
print("a = ",a, "\t" ,"b = ",b )
print("a == b   =   ", a == b )
print("a > b    =   ",a > b)
print("a < b    =   ",a < b)
print("a >= b    =   ",a >= b)
print("a <= b    =   ",a <= b)
print("a != b    =   ",a != b)
print("****************************************************************************")
print("\n")
print("\t LETS KNOW ABOUT CONDITIONAL OPERATORS \t:\n")
print("\t\tIF - Else Statements : \n")
print("a = ",a, "\t" ,"b = ",b )
if a > b :
    print("a > b    =   ", a > b)
else :
    print("a <= b    =   ", a <= b)



print("\n")
grade = 92
if grade >= 90:
    letterGrade = "A"
elif grade >=80:
    letterGrade = "B"

print("Percentage is %d " % grade )
print ("GRADE = %c" % letterGrade )



print("\t\tNESTED IF-Else Statements : \n")
print("\n")
c = 0
print("a = ", a, "\t", "b = ", b,"\t","c = ",c)
if (a > b and a > c) :
    print("GREATEST VALUE IS    ",a)
elif (b > a and b > c) :
    print("GREATEST VALUE IS     ",b)
else:
    print("GREATEST VALUE IS     ",c)

print("\n")
Value=50
print("Value = ",Value)
if Value < 200:
    print("Value is less than 200")
    if Value < 150:
        print("Value is less than 150")
        if Value < 100:
            print("Value is less than 100")
            if Value == 50:
                print("Value is 50")



print("\n")
print("\t\tUse of Ternary Operator : \n")
age = 17
print("AGE is %d" %age)
print('Eligible to buy Alcohal' if age>= 18 else 'Ineligible to buy Alcohal')

print("\n")
print("\t\tUse of WHILE-Condition : \n")

num = 2
print("Table of %d" %num)
while(num <= 20) :
    print("%d" %num)
    num += 2

#print("\n")
#print("\t\tUse of Continue-Condition : \n")

#mlist = ['Rakesh Yadav']

#for letter in mlist :
 #   print( letter ,sep="\n")
  #  if letter==" ":
   #     break








