#Aim : Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of the triangle are entered by the user.
# Developer : Rakesh Yadav

n1 = eval(input("Enter 1st-side of Triangle : "))
n2 = eval(input("Enter 2nd-side of Triangle : "))
n3 = eval(input("Enter 3rd-side of Triangle : "))


if n1 > 0 and n2 > 0 and n3 > 0 :
    if n1 == n2 and n2 == n3 :
        print("Equilateral Triangle")
    elif n1 == n2 or n1 == n3 :
        print("Isosceles Triangle")
    else :
        print("Scalene Triangle")
else:
    print("Invalid")
