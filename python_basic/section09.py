# Section09
# 파일 다루기

# 읽기 모드 : r
# 쓰기 모드 (기존 파일 삭제) : w
# 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로
# . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1
f = open('D:/코딩/Python/python_basic/resource/review.txt', 'r')
contents = f.read()
print(contents)
print(dir(f))

f.close() # open 후 반드시 자원 반환

print("---------------------")
print("---------------------")

# 에제 2
# with문이 끝나면 자동으로 리소스 반환
# 예제 1 코드와 같다
with open('D:/코딩/Python/python_basic/resource/review.txt', 'r') as f:
  c = f.read()
  print(c)
  print(iter(c))
  print(list(c))

print("---------------------")
print("---------------------")

with open('D:/코딩/Python/python_basic/resource/review.txt', 'r') as f:
  for c in f:
    # 라인 단위로 출력
    print(c)

    # 양쪽 공백과 줄바꿈제거
    print(c.strip())

print("---------------------")
print("---------------------")

# 예제 3
with open('D:/코딩/Python/python_basic/resource/review.txt', 'r') as f:
  content = f.read()
  print(">", content)

  # 한 번 읽은 후에는 파일을 읽는 커서가 내용 맨 끝에 있으므로 읽어오는 내용이 없다.
  content = f.read()
  print(">", content)

print("---------------------")
print("---------------------")

# 예제 4
with open('D:/코딩/Python/python_basic/resource/review.txt', 'r') as f:
  print("readline")
  line = f.readline()

  while line:
    print(line, end='##')
    line = f.readline()
print()
print("---------------------")
print("---------------------")

# 예제 5
with open('D:/코딩/Python/python_basic/resource/review.txt', 'r') as f:
  contents = f.readlines() # 모든 문장을 리스트 형태로 가지고 있는다 라인단위로
  print(contents)

  for c in contents:
    print(c, end='******')

print()
print("---------------------")
print("---------------------")

# 예제 6
score = []
with open('D:/코딩/Python/python_basic/resource/score.txt', 'r') as f:
  for line in f :
    
    score.append(int(line)) # txt 파일에 저장된 내용은 무조건 문자열로 취급
  print(score)

print('Averae : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제 1
with open('D:/코딩/Python/python_basic/resource/text1.txt', 'w') as f:
  f.write('Niceman!\n')

with open('D:/코딩/Python/python_basic/resource/text1.txt', 'a') as f:
  f.write('Goodman!\n')

with open('D:/코딩/Python/python_basic/resource/text2.txt', 'a') as f:
  f.write('NiceGoodman!\n')

# 예제 2
from random import randint
with open('D:/코딩/Python/python_basic/resource/text3.txt', 'w') as f:
  for cnt in range(6):
    f.write(str(randint(1, 50))) # 1~50 까지의 랜덤 숫자 생성
    f.write('\n')

# 예제 3
# writelines : 리스트 -> 파일로 저장
with open('D:/코딩/Python/python_basic/resource/text4.txt', 'w') as f:
  list = ['Kim\n', 'Park\n', 'Cho\n']
  f.writelines(list)

# 에제 4
# console에 출력이 아니라 쓰기모드의 파일로 내용이 저장되어진다.
with open('D:/코딩/Python/python_basic/resource/text5.txt', 'w') as f:
  print('Test Contests1 !', file = f)
  print('Test Contests2 !', file = f)