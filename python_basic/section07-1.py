# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#   함수
#   함수
#   함수

# 예제1
class UserInfo:
  # 속성, 메소드

  # 생성자 역할
  def __init__(self, name):
    self.name = name
  
  def user_info_p(self):
    print("Name : ", self.name)

# 클래스, 인스턴스 차이 중요 
# 네임스페이스(객체(클래스)를 인스턴스화 할 때 저장된 인스터스 자기 자신만의 독립적인 공간, 즉 변수명과 객체를 연결하는 것), 모든 자료형은 네임스페이스를 가진다.
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용한다.

user1 = UserInfo("hoon")
user1.user_info_p()

user2 = user1
user2.user_info_p()

user3 = UserInfo("park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(id(user3))
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# 예제 2 
# self의 이해
# 인스턴스는 호출 시 메서드에 자기 자신의 인스턴스를 넘기는데 그것이 self
class SelfTest:
  # 클래스 메서드 : 인스턴스에서 접근 불가능, 클래스에서 직접 호출
  def function1():
    print('functional called!')

  # 인스턴스 메서드 : 인스턴스 생성 후에 인스턴스로 접근 가능
  def function2(self):
    print(id(self))
    print('functional called2!')

self_test = SelfTest()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# 예제3 
# 클래스 변수, 인스턴스 변수
class WareHouse:
  # 클래스 변수
  # 여러 인스턴스에서 공유
  stock_num = 0 

  # 인스턴스 생성시에 init 호출 구현 안할 시 자동 호출된다.
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num += 1
  
  # 소멸자 객체가 더 이상 필요없을 때 자동 호출
  def __del__(self):
    WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(id(user1))
print(id(WareHouse))

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)
