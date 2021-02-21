# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 1. 기본출력(아래 방법 모두 문자열 취급)
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print() # 줄바꿈 효과

# 2. Separator 옵션 사용
print('T', 'E', 'S', 'T') # sep 생략시 기본값은 공백 한 칸이다. 
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# 3. End 옵션 사용
print('welcome To') # end 생략시 기본값은 줄바꿈이다.
print('welcome To', end=' ')
print('the black parade')
print('piano notes')

print()

# format 사용 [], {}, () -> 대, 중, 소
print('{} and {}'.format("""You""", 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'You', b = 'Me'))

  # %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is 7" % 'hoon')
print("%s's favorite number is %d" % ('hoon', 7))

  # %5d : 5자리를 확보한 후 오른쪽 정렬
  # %05d : 5자리를 확보한 후 오른쪽 정렬, 왼쪽의 빈칸들은 0으로 채운다
  # %.2f : 소수 둘째 자리까지 출력된다.(세번째 자리에서 반올림 되어 출력), 반올림 대상이 절반에 걸리는 경우(5) 가까운 짝수로 맞춰준다. 0.5는 0, 1.5와 2.5는 2가 되는 식이다. 
print("Test1 : %5d, Price: %4.2f" %(776, 6534.123))
print("Test1 : %05d, Price: %4.2f" %(776, 6534.126))

  # format에서는 %를 쓸때와 다르게 자동형변환이 이루어지지 않는다.
print("Test1 : {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("test1 = %d" % 5.3)
print("Test1 : {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))\


# Escape 코드
"""
\n : 개행 (중요)
\t : 탭 (중요)
\\ : 문자 (중요)
\' : 문자 (중요)
\" : 문자 (중요)
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
  # 따옴표간의 쌍이 잘 맞아야한다.
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\')
print('\\you\\\n\n\n\n')
print('\t\t\t\ttest')