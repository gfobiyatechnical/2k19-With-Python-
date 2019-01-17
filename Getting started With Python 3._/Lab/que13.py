#Aim : Program to find the Simple Interest and the total amount when the Principal, Rate of Interest and Time are entered by the user.
# Developer : Rakesh Yadav

Principal = eval(input("Enter Principal Amount : "))
Rate = eval(input("Enter Rate : "))
Time = eval(input("Enter Time : "))

Simple_Interest = ( Principal * Rate * Time ) / 100
print("Simple Interest = ",Simple_Interest)
