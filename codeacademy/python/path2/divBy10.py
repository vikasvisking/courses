#Write your function here
def divisible_by_ten(nums):
  amount = 0
  for number in nums:
    if number % 10 == 0:
      amount += 1
  return amount
  
  

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))