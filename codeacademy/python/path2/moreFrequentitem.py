#Write your function here
def more_frequent_item(lst, item1, item2):
  item1_count = lst.count(item1)
  item2_count = lst.count(item2)
  if item1_count > item2_count:
    return item1
  elif item2_count > item1_count:
    return item2
  else:
    return item1
    

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))