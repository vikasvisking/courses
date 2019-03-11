first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name , last_name):
  fname_length = len(first_name)
  lname_length = len(last_name)
  return first_name[fname_length - 3:] + last_name[lname_length - 3:]

temp_password = password_generator(first_name , last_name)