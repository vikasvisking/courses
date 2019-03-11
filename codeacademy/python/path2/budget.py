# Write your over_budget functid
def over_budget(budget, food, electricity_bill, internet_bill, rent):
  if budget < ( food+ electricity_bill + internet_bill+ rent):
    return True
  else:
    return False

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True