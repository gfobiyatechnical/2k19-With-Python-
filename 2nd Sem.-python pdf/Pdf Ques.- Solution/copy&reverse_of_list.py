# author: Rakesh yadav
# aim: Make a copy of the same string in reverse order

l = list(input("Enter a string value:  "))
new_string = list(reversed(l)) # new_string = l[:] - also give reversed of any list...
print(new_string)
