"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
	if element < 5 :
		print(element)


# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

newList = []
for element in a:
	if element < 5:
		newList.append(element)
print(newList)

# Write this in one line of Python.

newlist = [i for i in a if i<5]
print (newlist)

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

number = int(input("please enter a number: "))
lst = [i for i in a if i< number]
print(lst)