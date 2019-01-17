'''
Aim :  Program to input two numbers and subtract the smaller number from the greater number.

Developer : Rakesh Yadav
'''

n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))

if n1 > n2 :
    print( n1,"-",n2,' = ', (n1-n2) )
elif n2 > n1 :
    print( n2,'-',n1,' = ',(n2-n1) )
else:
    print('Both values are equal.')
