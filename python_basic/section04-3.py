# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 (순서O, 중복O, 수정O, 삭제O)
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c + e)
print(c * 3)
print(str(c[0]) + 'hi') 
# print("c[0] + 'hi' - ", c[0] + 'hi') # 문자형 + 정수형 불가

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:3] = [] # 기존 슬라이싱에 값 대입
print(c)
c[1:2] = [100, 1000, 50]
print(c)

del c[1] # 특정 인덱스의 값 삭제
print(c)
del c[-1]
print(c)

# 리스트 함수
# 삭제 : del, remove, pop
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 맨 끝에 요소 추가
print(y)
y.sort() # 오름차순 정렬
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2) # del과 다르게 특정 값을 찾아 삭제
y.remove(7)
print(y)
b = y.pop() # 맨 마지막 요소 삭제 후 그 요소를 반환한다.
print(b)
print(y)

ex = [88, 77]
y.append(ex) # 요소의 자료 그 자체를 삽입한다.
print(y)
y.extend(ex) # append와 달리 자료의 요소들만 삽입한다.
print(y)

# 튜플 (순서O, 중복O, 수정X, 삭제X)
a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()

# 튜플 함수
z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)
print(z.index(1)) # 값에 해당하는 첫 번째 요소의 인덱스 반환
print(z.count(1)) # 값에 해당하는 요소의 갯수 반환