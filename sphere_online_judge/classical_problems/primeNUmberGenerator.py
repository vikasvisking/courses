

def primeNumberGenerator(a , b):
	num_list = []
	for i in range(a, b+1):
		for j in range(2,b+1):
			if i%j == 0 :
				if i not in num_list and i != j:
					num_list.append(i)
				continue
		if i not in num_list:
			print(i)

c = int(input())
d =  input()
new_list = d.split(" ")
a = int(new_list[0])
b = int(new_list[1])


if a < b :
	primeNumberGenerator(a,b)
else:
	primeNumberGenerator(b,a)
				
