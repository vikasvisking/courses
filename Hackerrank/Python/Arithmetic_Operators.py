# Task
#
# Read two integers from STDIN and print three lines where:
#
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.

# solution:

if __name__ == '__main__':
    a = int(input())
    b = int(input())

c = a + b
d = a - b
e = a*b
print(c)
print(d)
print(e)
