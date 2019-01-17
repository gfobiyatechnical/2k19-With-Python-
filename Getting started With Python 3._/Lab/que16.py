'''

Aim :  Program to input the number of overs in a Cricket match and output the maximum runs a
        player can score in the match. Assume that there are no extra runs or NO balls in the match
        played. For example, in a 50 over match, the maximum runs scored are 1653.
Developer : Rakesh Yadav

'''

overs = int(input("Enter number of over : "))

''' logic to calculate runs in given overs '''

overs = overs // 2
runs = overs * 36
runs = runs + overs * 30 + 3

print("Maximum Runs can be Scored is %d" %runs )
