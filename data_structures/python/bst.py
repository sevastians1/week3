class Bst:
  def __init__(self):
    self.parent = None
    pass

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    if self.parent is None:
      self.parent = Node(value)
    else:
      top_node=self.parent
      while value:
        new_node=Node(value)
        # print(top_node.data, new_node.data)
        # print(top_node.left, top_node.right)
        if value>top_node.data:##big num
          # print("bigger")
          if top_node.right==None:
            top_node.right=new_node
            return
          else:
            top_node=top_node.right
        elif value<top_node.data:##little num
          # print("smaller")
          if top_node.left==None:
            top_node.left=new_node
            return
          else:
            top_node=top_node.left
    

  def contains(self, value):
    top_node=self.parent
    while value!=top_node.data:
      if value>top_node.data:
        top_node=top_node.right
      elif value<top_node.data:
        top_node=top_node.left
    print(top_node.data)
    return top_node.data


  def remove(self, value):
    # this is where you will remove a value from the BST
    pass



# ----- Node ------
class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None
  def left(self, left):
    self.left= left
  def right(self, right):
    self.right= right
  def define_data(self):
    return self.data
  
none=Bst()
none.insert(10)
none.insert(115)
none.insert(5)
none.insert(2)
none.insert(61)
none.contains(2)
