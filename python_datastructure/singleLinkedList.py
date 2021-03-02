class Node :
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class SingleLinkedList :
  def __init__(self) :
    self.head = None
    self.tail = None

  def append(self, data) :
    current_node = Node(data)

    if self.head == None:
      self.head = current_node
      self.tail = current_node
    else:
      self.tail.next = current_node
      self.tail = current_node
      
  def search(self) :
    current_node = self.head

    while current_node :
      print(current_node.data)
      current_node = current_node.next
  
  def delete(self, data) : 
    if self.head.data == data:
      temp = self.head
      self.head = self.head.next
      del temp
    else:
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp

          if node.next == None:
            self.tail = node

          return
        else:
          node = node.next


test_list = SingleLinkedList()
test_list.append(3)
test_list.append(6)
test_list.append(9)
test_list.delete(3)
test_list.search()
print(test_list.tail.data)