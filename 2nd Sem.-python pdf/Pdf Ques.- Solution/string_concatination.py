'''
author: Rakesh yadav
aim: Given a string name, e.g. "Bob",
     return a greeting of the form "Hello Bob!".
     helloName("Bob") → "Hello Bob!"
     helloName("Alice") → "Hello Alice!"
     helloName("X") → "Hello X!"
'''

name = input("Enter any name: ")
prefix = "hello "
print(prefix + name)
