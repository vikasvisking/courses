from node import Node

# Add your Stack class below:

class Stack:
  def __init__(self, top_item = None):
    self.top_item = top_item
    
  def peek(self):
    return self.top_item.get_value()