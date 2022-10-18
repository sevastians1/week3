list=[]
class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head):
    self.head=Node(head)
    self.length=0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    # if self.length==0:
    # print(self.head.data, self.head.previous, self.head.next)
    new_node=Node(data)
    new_node.set_next(self.head)
    if self.head != None:
      self.head.previous=new_node
    self.head=new_node




  def remove_at_data(self, data):
    first_item=self.head
    while first_item != None:
      # print(first_item.data)
      if first_item.data == data:
        first_item.previous.next=first_item.next
        first_item.next.previous=first_item.previous
        return
      first_item=first_item.next

  def printval(self):
    first_item=self.head
    while first_item != None:
      print(first_item.data, first_item.next, first_item.previous)
      first_item=first_item.next

  def get_length(self, index):
    # write you code to GET and return an element from the Linked List
    length=0
    first_item=self.head
    while first_item!= None:
      if length==index:
        print(first_item.data)
        return first_item.data
      length+=1
      first_item=first_item.next


  # def remove_at_length(self, length):
  #   first_item=self.head
  #   while first_item != None:
  #     print(first_item.length)
  #     if first_item.length == length:
  #       pass

# ----- Node ------
class Node:
  def __init__(self, data):
    self.data=data
    self.next=None
    self.previous=None

  def get_data(self):
    return self.data

  def set_data(self, data):
    self.data=data

  def get_next(self):
    return self.next

  def set_next(self, next):
    self.next=next
  def set_previous(self, previous):
    self.previous=previous


list=LinkList(6)
list.add(5)
list.add(4)
list.add(3)
list.add(2)
list.add(1)
# list.remove_at_data(3)
# list.printval()
list.get_length(3)
# list.remove_at_data(4)
# print(list.get_length())
