#Aim : Program to find the Compound Interest compounded annually and the total amount when the Principal, Rate of Interest and Time are entered by the user
# Developer : Rakesh Yadav


Principal = eval(input("Enter Principal Amount : "))
Rate = eval(input("Enter Rate : "))
Time = eval(input("Enter Time : "))
Compound_Interest = Principal*( 1 + (Rate / Time) )**Time
print("Compound Interest = %.2f" % Compound_Interest )
