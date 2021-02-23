# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합

# 딕셔너리(Dictionary) : 순서x, 중복x(키는 중복x, 값은 중복o), 수정o, 삭제o
# 선언
a = {
  'name':'kim',
  'phone':'010-7777-7777',
  'birth':870214,
  'date':870214
}

b = {
  0 : 'Hello Python',
  1 : 'Hello Coding'
}

c = {
  'arr' : [1, 2, 3, 4, 5]
}

# 출력
print(a['name'])
print(a.get('name'))
# print(a['name2']) => 에러발생
print(a.get('name2')) # None 처리
print(type(c['arr']))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

# Keys, Values, Items(키와 값의 한 쌍을 말한다.)
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
temp = list(a.values())
print(temp[5])
print(temp[5][1])

print(a.items())
print("11111")
print(list(a.items())) # 리스트안에 튜플로 키와값 저장된다.
print(1 in b) # 키 값을 조회
print('name' not in a) # 키 값을 조회

# 집합(Set) (순서x, 중복x, 수정x(값 추가는 가능), 삭제o)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6]) 

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(l)
print('---')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1 | s2) # 합집합
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s1.difference(s2)) # 차집합

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)
s3.remove(15)
print(s3)
print(type(s3))