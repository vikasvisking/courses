#Write your function here
def middle_element(lst):
  count = len(lst)
  if count % 2 == 1:
    index = int(count/2)
    return lst[index]
  else:
    index = int(count/2)
    average =( lst[index] + lst[index - 1])/2
    return average
  
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))