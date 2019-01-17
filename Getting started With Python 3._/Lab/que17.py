'''

Aim :  Program to input the number of heads and feet in a farm and identify the number of chickens
        and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150
        chickens and 190 goats.

Developer : Rakesh Yadav

'''

heads = int(input("Enter no. Heads : "))
feets = int(input("Enter no. of Feets : "))

''' logic Random input for number of goats '''
import random
goats = random.randrange(1,heads)
chickens = heads - goats

goat_feets = goats * 4
chicken_feets = chickens * 2

if feets == (goat_feets + chicken_feets ) :
    print("%d chickens and %d goats" %(chickens,goats))
else :
    print('TRY AGAIN .... ')

