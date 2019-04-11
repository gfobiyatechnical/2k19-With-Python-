'''
author: Rakesh yadav
aim: Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string
     length will be at least 2.
     extraEnd("Hello") → "lololo"
     extraEnd("ab") → "ababab"
     extraEnd("Hi") → "HiHiHi"
'''
srt = input("Enter any string:  ")
print(srt[-2::]*3)  #logic to get last 2 strings 3 times.

print(srt[2:4:1])   #to get string b/w 1 to 4 indices.

#to interchange first with last latter of string.
srt=list(srt)
m=srt[5]
srt[5]=srt[0]
srt[0]=m
print(srt)
