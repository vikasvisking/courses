#Write your function here
def larger_sum(lst1, lst2):
  items = 0
  elements = 0
  for item in lst1:
    items += item 
  for element in lst2:
    elements += element
  if items > elements:
    return lst1
  elif elements > items:
    return lst2
  else:
    return lst1
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))