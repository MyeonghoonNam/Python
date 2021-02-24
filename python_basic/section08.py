# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리


# 사용1 (클래스)
# from 폴더와 파일 import 클래스나 메소드
from package.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용2 (권장하지않음, 메모리 많이 사용)
# 모든 모듈들을 가져온다
from package.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용3 (클래스)
# Alias 설정 -> as 별칭 : 별칭으로 클래스 접근 가능하다.
from package.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex3 : ", fb.fib2(400))
print("ex3 : ", fb().title)

# 사용4(함수)
import package.calculations as c
print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
from package.calculations import div as d
print("ex5: ", int(d(100,9)))

# 사용6
import package.prints as p
import builtins # 기본적으로 임포트 되는 함수로써 생략가능(파이썬기본내장함수)
p.prt1()
p.prt2()
# dir() : 객체가 어떤 변수와 메소드를 가지고 있는지 리스트로 나열해준다.
print(dir(builtins))

# __init__.py
# 용도 : 해당 디렉토리가 패키지임을 선언한다.(2.x 버전)
# Python 3.x : 파일이 없어도 패키지 인식한다. -> 그러나 하위호환 위해서 생성해 놓는것을 추천한다.