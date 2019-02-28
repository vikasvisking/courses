#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = raw_input("please enter your name: ")
age = int(input("please enter your age: "))
print( name +" will turn 100 years old in " + str((2019 - age) + 100))