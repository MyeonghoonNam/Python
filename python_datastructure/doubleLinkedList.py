class Node :
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else : 
      curNode = self.head
      
      while curNode.next :
        curNode = curNode.next
      
      newNode = Node(data)
      curNode.next = newNode
      newNode.prev = curNode
      
      self.tail = newNode

  def desc(self):
    curNode = self.head

    while curNode:
      print(curNode.data)
      curNode = curNode.next

  def search_head(self, data):
    if self.head == None:
      return False

    curNode = self.head

    while curNode :
      if curNode.data == data :
        return curNode
      else :
        curNode = curNode.next

    return False

  def search_tail(self, data):
    if self.head == None:
      return False

    curNode = self.tail
    while curNode :
      if curNode.data == data :
        return curNode
      else :
        curNode = curNode.prev

    return False

  def insert_prev(self, data, find_data):
    if self.head == None:
      self.head = Node(data)
      return True

    curNode = self.tail
    while curNode.data != find_data :
      curNode = curNode.prev
      
      if curNode == None:
        return False
      
    newNode = Node(data)

    temp = curNode.prev
    curNode.prev = newNode
    newNode.next = curNode
    newNode.prev = temp
    temp.next = newNode

    return True

  def insert_next(self, data, find_data):
    if self.head == None:
      self.head = Node(data)
      return True

    curNode = self.head
    while curNode.data != find_data:
      curNode = curNode.next
      if curNode == None:
        return False
      
    newNode = Node(data)

    temp = curNode.next
    curNode.next = newNode
    newNode.prev = curNode
    newNode.next = temp
    temp.prev = newNode

    if temp.next == None:
      self.tail = temp

    return True

dll = DoubleLinkedList()
dll.insert(3)
dll.insert(6)
dll.insert(9)
dll.desc()
dll.insert_prev(7, 9)
dll.desc()
node = dll.search_head(7)
print(node.data)
dll.insert_next(8, 7)
dll.desc()