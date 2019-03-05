# problem: YYour program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

# your code goes here


# solution

while 1:
	a = int(raw_input())
	if a == 42:
		break
	print (a)