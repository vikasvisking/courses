#Write your function here
def over_nine_thousand(lst):
  items = 0
  for item in lst:
    if items <= 9000:
      items += item
  return items
  
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))