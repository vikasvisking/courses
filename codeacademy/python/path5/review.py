def username_generator(first_name , last_name):
  return first_name[:3] + last_name [:4]

def password_generator(username):
  password = ""
  for i in range(len(username)):
    password += username[i-1]
    
  return password
    