from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def has_space(self):
    if self.limit > self.size:
      return True
    
  
    
  def push(self, value):
    
    if self.has_space() :
    	item = Node(value)
    	item.set_next_node(self.top_item)
    	self.top_item = item
    	# Increment stack size by 1 here:
    	self.size += 1
    else:
      print("All out of space")
    

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.size > 0:
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  def is_empty(self):
    if self.size == 0:
      return True
      
  # Define has_space() and is_empty() below:
  