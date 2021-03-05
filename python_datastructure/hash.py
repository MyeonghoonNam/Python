############################################
# def hashFunc(key):
#   return key % 5

# hashTable = [0 for i in range(10)]
# print(hashTable)

# def storageData(data, value):
#   key = ord(data[0])
#   hashAddr = hashFunc(key)
#   hashTable[hashAddr] = value

# def getData(data):
#   key = ord(data[0])
#   hashAddr = hashFunc(key)
#   return hashTable[hashAddr]

# storageData('Andy', '01055553333')
# storageData('Dave', '01044443333')
# storageData('Trump', '01022223333')

# print(hashTable)
# print(getData('Andy'))

############################################

# chaining 기법
# hashTable = [0 for i in range(10)]

# def getKey(data):
#   return hash(data)

# def hashFunc(key):
#   return key % 8

# def saveData(data, value):
#   key = getKey(data)
#   hashAddr = hashFunc(key)
#   if type(hashTable[hashAddr]) is list :
#     for idx in range(len(hashTable[hashAddr])):
#       if hashTable[hashAddr][idx][0] == key:
#         hashTable[hashAddr][idx][1] = value
#     hashTable[hashAddr].append([key, value])
#   else:
#     hashTable[hashAddr] = [[key, value]]

# def readData(data):
#   key = getKey(data)
#   hashAddr = hashFunc(key)

#   if type(hashTable[hashAddr]) is list:
#     for idx in range(len(hashTable[hashAddr])):
#       if hashTable[hashAddr][idx][0] == key:
#         return hashTable[hashAddr][idx][1]
#     return None
#   else:
#     return None

# saveData('Dave', '0102030200')
# saveData('Andy', '01033232200')
# print(readData('Dave'))
# print(hashTable)

###############################################

# Linear Probing 기법
hashTable = [0 for i in range(10)]

def getKey(data):
  return hash(data)

def hashFunc(key):
  return key % 8

def saveData(key, value):
  key = getKey(key)
  hashAddr = hashFunc(key)

  if hashTable[hashAddr] != 0:
    for idx in range(hashAddr, len(hashTable)):
      if hashTable[idx] == 0:
        hashTable[idx] = [key, value]
        return
      elif hashTable[idx][0] == key:
        hashTable[idx][1] = value
        return
  else:
    hashTable[hashAddr] = [key, value]

def readData(key):
  key = getKey(key)
  hashAddr = hashFunc(key)

  if hashTable[hashAddr] != 0:
    for idx in range(hashAddr, len(hashTable)):
      if hashTable[idx] == 0:
        return None
      elif hashTable[idx][0] == key:
        return hashTable[idx][1]
  else:
    return None

saveData('dk', '01200123123')
saveData('da', '3333333333')
saveData('db', '3333333333')
saveData('dc', '3333333333')
saveData('dd', '3333333333')
saveData('de', '3333333333')
saveData('df', '3333333333')
saveData('dg', '3333333333')
saveData('dh', '3333333333')
saveData('di', '3333333333')
saveData('dj', '3333333334')
print(readData('zc'))
print(readData('da'))
print(hashTable)