# Aim : To make Simple Calculator
# Author : Rakesh Yadav

pri_ammount = float(input("Enter principle ammount: "))
rate = float(input("Enter the ammount of rate of intrest: "))
time = float(input("Enter time period: "))

#Calculation for simple intrest
SI = ((pri_ammount*rate*time) / 100)

#Calculation for compound  intrest
CI =  (pri_ammount *(1 + rate/100)**time)

choice = int(input("CHOOSE 1  TO CALCULATE: CI\tCHOOSE 2  TO CALCULATE: SI  "))
if choice == 1 :
    print("Your Simple Intrest is %.2f " %CI)
elif choice == 2 :
    print("Your Compund Intrest is %.2f " % SI)
else :
    print("Invallid Entary: ****Try Again****\n")






