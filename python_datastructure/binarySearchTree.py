class Node :
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Bst :
  def __init__(self, head):
    self.head = head

  def insert(self, value):
    curNode = self.head

    while True:
      if value < curNode.value:
        if curNode.left != None:
          curNode = curNode.left
        else :
          curNode.left = Node(value)
          break
      elif value > curNode.value:
        if curNode.right != None:
          curNode = curNode.right
        else :
          curNode.right = Node(value)
          break
      else:
        print("중복된 값이 이미 트리에 존재합니다.")
        break

  def search(self, value):
    curNode = self.head

    while curNode :
      if curNode.value == value:
        # print(curNode.value)
        return True
      elif curNode.value < value:
        curNode = curNode.right
      else :
        curNode = curNode.left
  
  def delete(self, value):
    searched = False
    curNode = self.head
    parNode = self.head

    while curNode:
      if curNode.value == value:
        searched = True
        break
      elif value < curNode.value:
        parNode = curNode
        curNode = curNode.left
      else :
        parNode = curNode
        curNode = curNode.right

    if searched == False:
      print("해당 값을 가지는 노드가 없습니다.")
      return False

    # case 1 : 삭제할 Node가 Leaf Node인 경우
    if curNode.left == None and curNode.right == None:
      if value < parNode.value:
        parNode.left == None
      else :
        parNode.right == None

    # case2: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
    # 왼쪽에만 노드가 있는 경우
    elif curNode.left != None and curNode.right == None:
      if value < parNode.value:
        parNode.left = curNode.left
      else :
        parNode.right = curNode.left
    # 오른쪽에만 노드가 있는 경우
    elif curNode.left == None and curNode.right != None:
      if value < parNode.value :
        parNode.left = curNode.right
      else :
        parNode.right = curNode.right

    # case3-1 : 삭제할 Node가 Child Node를 두 개 가지고 있을 경우 (삭제할 Node가 Parent Node 왼쪽에 있을 때
    elif curNode.left != None and curNode.right != None:
      if value < curNode.value:
        chgNode = curNode.right
        chgNode_Parent = curNode.right
        
        while chgNode.left != None:
          chgNode_Parent = chgNode 
          chgNode = chgNode.left
        
        if chgNode.right != None:
          chgNode_Parent.left = chgNode.right
        else :
          chgNode_Parent.left = None

        parNode.left = chgNode
        chgNode.left = curNode.left
        chgNode.right = curNode.right
      else :
        chgNode = curNode.right
        chgNode_Parent = curNode.right

        while chgNode.left != None:
          chgNode_Parent = chgNode
          chgNode = chgNode.left
        
        if chgNode.right != None:
          chgNode_Parent.left = chgNode.right
        else :
          chgNode_Parent.left = None
        
        parNode.right = chgNode
        chgNode.left = curNode.left
        chgNode.right = curNode.right

    return True

# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = Bst(head)
for num in bst_nums:
    binary_tree.insert(num)
    
# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
      print ('search failed', num)
    else :
      print ('search key :', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
      print('delete failed', del_num)
    else:
      print('delete key :', del_num)