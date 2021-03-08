class Node :
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree :
  def __init__(self):
    self.root = None

  def insert(self, data):
    self.root = self.insert_value(self.root, data)
    
    return self.root is not None
  
  def insert_value(self, node, data):
    if node is None:
      node = Node(data)
    else :
      if data < node.data:
        node.left = self.insert_value(node.left, data)
      elif data > node.data:
        node.right = self.insert_value(node.right, data)
      else :
        print("중복된 값이 이미 존재합니다.")
        return
    return node

  def find(self, data):
    return self.find_value(self.root, data)

  def find_value(self, node, data):
    if node is None or node.data == data :
      return node is not None
    elif data < node.data:
      return self.find_value(node.left, data)
    elif data > node.data:
      return self.find_value(node.right, data)
    
    # if node is None or node.data == data:
    #   return node is not None
    # elif data < node.data:
    #   return self.find_value(node.left, data)
    # else:
    #   return self.find_value(node.right, data)
  
  def delete(self, data):
    self.root, deleted = self.delete_value(self.root, data)
    return deleted
  
  def delete_value(self, node, data):
    if node is None:
      return node, False
    
    deleted = False
    
    if data == node.data:
      deleted = True

      if node.left and node.right:
        parent = node
        child = node.right

        while child.left is not None:
          parent = child
          child = child.left
        
        child.left = node.left

        if parent != node:
          parent.left = child.right
          child.right = node.right
        
        node = child
      elif node.left or node.right:
        node = node.left or node.right
      else :
        node = None
    elif data < node.data:
      node.left, deleted = self.delete_value(node.left, data)
    else :
      node.right, deleted = self.delete_value(node.right, data)

    return node, deleted
      
  
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
  bst.insert(x)

print(bst.root.left.right.left.data)
# Find
print(bst.find(15)) # True
print(bst.find(17)) # False
# # Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11))

  

