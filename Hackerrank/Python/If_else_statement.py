# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# solution

N = int(input())

if N%2 != 0:
    print('Weird')

elif 2 <= N <= 5:
    print('Not Weird')

elif 6<= N <= 20:
    print('Weird')

else:
    print('Not Weird')
