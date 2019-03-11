#Write your function here
def exponents(bases, powers):
  results = []
  for base in bases:
    for power in powers:
      result = base**power
      results.append(result)
  return results 
 
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))