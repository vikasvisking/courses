class Circle:
  pi = 3.14
  def __init__(self, diameter):
    self.radius = diameter/2 
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
  def circumference(self):
    circumference = 2* self.pi * self.radius
    return circumference
    
   
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())