# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = [] # 영어 단어 리스트

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('D:/코딩/Python/python_basic/resource/word.txt', 'r') as f:
  for c in f:
    words.append(c.strip()) # strip() : 문자열 양쪽 공백과 줄바꿈 삭제


# 사용자 입력 대기(입력값은 무조건 문자열로 들어간다.)
input("Ready? Press Enter Key!") # Ender Game Start!

# 현재 시각을 시작시간에 기록
start = time.time()

while n <= 5:
  random.shuffle(words) # 임의순서로 변경
  q = random.choice(words) # 목록중 랜덤으로 선택

  print()

  print("*Question # {}".format(n))
  print(q) # 문제출력

  x = input() # 타이핑 입력

  print()

  if(str(q).strip() == str(x).strip()):
    print("Pass!")
    cor_cnt += 1
  else:
    print("Wrong!")
  
  n += 1

end = time.time()
et = end - start
et = format(et, ".3f")


if cor_cnt >= 3:
  print("합격")
else:
  print("불합격")

print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
  pass
