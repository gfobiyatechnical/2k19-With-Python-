# Python code to chech the number is "prime number" or not...

number = int (input("Enter a number : "))


if number > 1 :
	for i in range (2, number):
		if number % i == 0 :
			print("%d not prime " %number)
			break
	else :
		print("%d is prime number" %number)
else :
	print("Enter positive number")

