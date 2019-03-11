from node import Node
# Create the Queue class below:


class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def peek(self):
    return self.head.get_value()
  