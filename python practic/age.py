#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = raw_input("please enter your name: ")
age = int(input("please enter your age: "))
message = name +" will turn 100 years old in " + str((2019 - age) + 100)
print(message)

num = int(input("how many time would you like to print the above line : "))

print( message * num)

print('\n')

print(" Yaa it seems messy..lets try again !")

num = int(input("how many time would you like to print the above line : "))
message += '\n'
print(message * num)