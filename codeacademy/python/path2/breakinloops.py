dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'


for breed in dog_breeds_available_for_adoption:
  print(breed)
  if dog_breed_I_want == breed:
    print("They have the dog I want!")
    break