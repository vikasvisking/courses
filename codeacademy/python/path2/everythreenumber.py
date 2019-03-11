#Write your function here
def every_three_nums(start):
  list_range = list(range(start,102 , 3))
  if start <= 100:
    return list_range
  else: 
    return []


#Uncomment the line below when your function is done
print(every_three_nums(91))