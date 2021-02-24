# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법

# def 함수명(parameter) :
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 선언 후에 호출이 가능하다 !

# 예제 1
def hello(world):
  print("Hello", world)

hello("Python!")
hello(7777)

# 예제 2
def hello_return(world):
  val = "Hello " + str(world)
  return val

str = hello_return("Python!!!!!")
print(str)

# 예제 3 (다중리턴)
def func_mul(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300

  return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제 4 (데이터 타입 반환)
def func_mul2(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300

  return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제 5
# 가변인자 *args, **kwargs
# * 한 개 일때는 튜플형태로 받는다, 2개 일 때는 딕셔너리로 받는다.

# *args : 매개변수의 다양한 형태(가변적)
def args_func(*args):
  for t in args:
    print(t)

def args_func2(*args):
  print(args)
  for i, v in enumerate(args):
    print(i, v)
    
def args_func3():
  for i, v in enumerate(range(10)):
    print(i, v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

args_func2('kim')
args_func2('kim', 'Park')
args_func2('kim', 'Park', 'Lee')

args_func3()

# **kwargs
def kwargs_func(**kwargs):
  for k, v in kwargs.items():
    print(k, v)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park')
kwargs_func(name1='kim', name2='park', name3='Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)
  print(len(args))

example_mul(10, 20)
example_mul('Lee', 20, 'park', 20, age1=24, age2=35)

# 중첩함수(클로저)
def nested_func(num):
  def func_in_func(num):
    print('>>>', num)
  print("in func")
  func_in_func(num + 10000)

nested_func(10000)

# 예제 6
# 코드상의 명시적 사용 지키지않아도 예외는 생기지 않는다.
def func_mul3(x : int) -> list:
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300

  return [y1, y2, y3]

print(func_mul3(5))

# 람다식  메모리 절약, 가독성 향상(지나치게 사용하면 가독성 저하, 주로 익명함수로 사용), 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int :
  return num * 10

var_func = mul_10 # 함수는 객체 생성 -> 리소스(메모리) 할당
print(var_func)
print(type(var_func))
print(var_func(10))

# 람다식 데이터전처리, DB나 웹 게시판의 대량 데이터 관리에 유리
lambda_mul_10 = lambda num : num * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
  return x * y * func(10)

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))

