#Write your function here
def append_sum(lst):
  add_last_two = lst[-2] + lst [-1]
  lst.append(add_last_two)
  add_last_two = lst[-2] + lst [-1]
  lst.append(add_last_two)
  add_last_two = lst[-2] + lst [-1]
  lst.append(add_last_two)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))