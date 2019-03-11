#Write your function here
def add_greetings(names):
  name = ["Hello, " + i for i in names]
  return name
  

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))