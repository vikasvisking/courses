#Write your function here
def combine_sort(lst1, lst2):
  combine_list= lst1 + lst2
  sorted_list = sorted(combine_list)
  return sorted_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))