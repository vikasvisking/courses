single_digits = [i for i in range (10)]
squares = []
cubes = [i**3 for i in single_digits]

for i in single_digits:
  squares.append(i**2)
  print(i)
  
print(squares)
print(cubes)
  
