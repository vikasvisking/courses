def contains(big_string , little_string):
  if little_string in big_string:
    return True
  else:
    return False
  
def common_letters(string_one , string_two):
  common = []
  for char in string_one:
    if (char in string_two) and (char not in common):
      common.append(char)
  return common
        
  