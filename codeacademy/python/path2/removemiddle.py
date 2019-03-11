#Write your function here
def remove_middle(lst, start, end):
  first_half = lst[:start]
  second_half = lst[end+1 :]
  list = first_half + second_half
  return list
  

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))