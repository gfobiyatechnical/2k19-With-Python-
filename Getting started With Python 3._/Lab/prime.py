# Python code to chech the number is "prime number" or not...

number = int (input("Enter a number : "))

# to checking number is positive or not ..
if number > 1 :
	# to find the prime number.... 
	for i in range (2, number):
		if number % i == 0 :
			print("%d not prime " %number)
			break
	else :
		print("%d is prime number" %number)
else :
	# display if number is not positive number....
	print("Enter positive number")

