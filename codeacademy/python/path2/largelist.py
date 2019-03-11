#Write your function here
def larger_list(lst1, lst2):
  list1_count = len(lst1)
  list2_count = len(lst2)
  if list1_count > list2_count:
    return lst1[-1]
  elif list1_count < list2_count:
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))