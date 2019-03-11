#Write your function here
def odd_indices(lst):
  newLst = []
  i = 0
  for item in lst:
    i +=1
    if (len(lst)>i and i % 2 == 1):
      newLst.append(lst[i]) 
  return newLst

# or


def odd_indices(lst):
  newlist = []
  for item in range(1 , len(lst), 2):
    newlist.append(lst[item])
  return newlist

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))