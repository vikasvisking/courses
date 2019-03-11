sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0 

for data in sales_data:
  for no in data:
    scoops_sold += no
    
print(scoops_sold)


