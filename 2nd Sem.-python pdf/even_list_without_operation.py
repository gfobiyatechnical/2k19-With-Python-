# author: Rakesh yadav
# aim: Print even numbers upto 100, without using any arithmetic or comparison operator.

l = list(map(int,range(100+1)))
num_list = l[0::2]
print(num_list)
