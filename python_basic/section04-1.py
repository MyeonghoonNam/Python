# 데이터 타입
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

bytearray
byte
frozenset
'''

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
  "name" : "Kim",
  "age" : 25
}

v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7] # 다른 언어에서는 배열

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))

"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939
f3 = .5
f4 = 10.
print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2, type(f3 + i2))

# 형변환

a = 5.
b = 4
c = 10

result2 = a + b
print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))
print(complex(True))

y = 100
y += 100 # y = y + 100
print(y)

# 수치 연산 함수
print(abs(-8)) # 절댓값
n, m = divmod(100, 8) # 몫은 n, 나머지는 m
print(n, m)

import math
print(math.ceil(5.1)) # 값 보다 크면서 가장 작은 정수
print(math.floor(3.874)) # 값 보다 작으면서 가장 큰 정수
