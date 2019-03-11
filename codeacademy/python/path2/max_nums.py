#Write your function here
def max_num(nums):
  item = nums[0]
  for num in nums:
    if num >= item:
      item = num
  return item
 
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))