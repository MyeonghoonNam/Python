# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy." # 공백도 1자리
str2 = 'NiceMan'
str3 = ' '
str4 = str() # 공백
str5 = str('ace') # 공백

# 객체의 길이(항목 수)를 반환한다. : len()
print(len(str1), len(str2), len(str3), len(str4), len(str5))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTat\tTab"
print(escape_str2)

# Raw String (경로)
raw_s1 = r'C:Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인 : 변수 다음에 \ 기호(escape) 표시 후 문자열("""안에만 가능)
# \ : 다음줄에 내용을 이어주는 기능
multi = \
"""
문자열
멀티라인
테스트
"""

print(multi)


# 문자열 연산
# 파이썬 문자열은 한 번 할당되면 수정이 불가능하다.(재할당은 가능)
# 할당 시 각자의 인덱싱이 이루어지기 때문에 수정 불가능
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print(str_o2 * 3)
print('a' in str_o4) # 문자열에 특정 문자 포함 여부, 포함 시 True 출력
print('f' not in str_o4) # 문자열에 특정 문자 포함 여부, 미포함 시 True 출력

# 문자열 형 변환
# print(77 + 'a') -> 문자형과 숫자형은 연산 불가
a1 = 88
b1 = "b"
print(str(a1) + b1)

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
a = 'Niceman'
b = 'orange'

print(a.islower()) # 모든 문자가 소문자인지 판별(모두 소문자이면 True)
print(b.endswith('e')) # 문자열의 마지막 문자를 판별
print(b.capitalize()) # 문자열의 첫 글자만 대문자 변환
print(a.replace('Nice', "Good"))
print(list(reversed(b))) # 리스트형의 요소들을 반대순서로 반환한다.

# 슬라이싱
print(a[0:3])
print(a[:])
print(a[0:len(a)])
print(b[0:5:2]) # [a:b:c] => a는 초기값, b-1은 마지막 값, c는 증감값 모두 생략가능
print(b[0:4:2])
print(b[1:-2]) # 맨 끝 문자열 인덱스는 -1로 표현가능, 즉 여기서는 1(r) 부터 -3(n)까지 출력
print(b[::-1]) # 역순 출력)