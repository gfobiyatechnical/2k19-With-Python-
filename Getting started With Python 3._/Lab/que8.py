
#Aim : Program to find the area and circumference of a circle, when the radius is entered by the user. However, the user can input radius in integer or float.
#Developer: Rakesh yadav


R = float (input("Enter Radius of Circle : "))


	# calculation
area = 3.14*(R * R)
circumference = 2 * 3.14 * R

print(" Circumference of a circle = %.2f" %(circumference))
print(" Area of circle = %.2f" %(area))



