def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2018 ,1993)

dads_age = calculate_age(2018 , 1953)

print("I am " + str(my_age) + " and my dad is " + str(dads_age) + "years old")