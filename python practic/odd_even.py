"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

number = int(input("please enter the number:" ))
if number % 4 == 0:
	print("number is divisible by 4")
if number%2 == 0:
	print(str(number) + ' is an even number')
else:
	print(str(number) + ' is an odd number')

"""Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

num = int(input("enter a number to check: "))
check = int(input("enter a number u want to divide check: "))
divide = num / check

if divide % 2 == 0:
	print("check divide the number evenly")

else:
	print("its not divided evenly")