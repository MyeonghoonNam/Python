class Heap:
  def __init__(self, data):
    self.heap = list()
    self.heap.append(None)
    self.heap.append(data)

  def moveUp(self, inserted_idx):
    if inserted_idx <= 1:
      return False
    
    prarent_idx = inserted_idx // 2

    if self.heap[inserted_idx] > self.heap[prarent_idx] :
      return True
    else :
      return False

  def moveDown(self, popIdx):
    leftChildPopIdx = popIdx * 2
    rightChildPopIdx = popIdx * 2 + 1

    # case 1 : 자식노드가 없는 경우
    if leftChildPopIdx >= len(self.heap):
      return False
    # case 2 : 왼쪽자식노드만 있는 경우
    elif rightChildPopIdx >= len(self.heap):
      if self.heap[popIdx] < self.heap[leftChildPopIdx]:
        return True
      else:
        return False
    # case 3 : 왼쪽, 오른쪽 자식 모두 있을 때
    else:
      if self.heap[leftChildPopIdx] > self.heap[rightChildPopIdx]:
        if self.heap[popIdx] < self.heap[leftChildPopIdx]:
          return True
        else:
          return False
      else:
        if self.heap[popIdx] < self.heap[rightChildPopIdx]:
          return True
        else:
          return False

  def insert(self, data):
    if len(self.heap) == 0:
      self.heap.append(None)
      self.heap.append(data)

    self.heap.append(data)

    inserted_idx = len(self.heap) - 1
    while self.moveUp(inserted_idx):
      parent_idx = inserted_idx // 2

      self.heap[parent_idx], self.heap[inserted_idx] = self.heap[inserted_idx], self.heap[parent_idx]

      inserted_idx = parent_idx
    
    return True

  def pop(self):
    if len(self.heap) <= 1:
      return None
    
    popData = self.heap[1]
    self.heap[1] = self.heap[-1]
    del self.heap[-1]
    popIdx = 1

    while self.moveDown(popIdx):
      leftChildPopIdx = popIdx * 2
      rightChildPopIdx = popIdx * 2 + 1

      if rightChildPopIdx >= len(self.heap):
        if self.heap[popIdx] < self.heap[leftChildPopIdx]:
          self.heap[popIdx], self.heap[leftChildPopIdx] = self.heap[leftChildPopIdx], self.heap[popIdx]
      else:
        if self.heap[leftChildPopIdx] > self.heap[rightChildPopIdx]:
          if self.heap[popIdx] < self.heap[leftChildPopIdx]:
            self.heap[popIdx], self.heap[leftChildPopIdx] = self.heap[leftChildPopIdx], self.heap[popIdx]
            popIdx = leftChildPopIdx
        else:
          if self.heap[popIdx] < self.heap[rightChildPopIdx]:
            self.heap[popIdx], self.heap[rightChildPopIdx] = self.heap[rightChildPopIdx], self.heap[popIdx]
            popIdx = rightChildPopIdx
    
    return popData



heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
data = heap.pop()
print(heap.heap)
print(data)