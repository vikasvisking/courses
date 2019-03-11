#Write your function here
def reversed_list(lst1, lst2):
  lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[len(lst1) - 1 - index]:
      lst.append('True')
  if len(lst) == len(lst1):
    return True
  else:
    return False
    

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))