# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 자식에서 부모의 모든 속성, 메소드 사용가능
# 상속을 통하여 코드 중복 방지 및 코드 재사용이 용이하다.

class Car:
  """Parent Class"""
  def __init__(self, tp, color):
    self.type = tp
    self.color = color
  
  def show(self):
    return 'Car Class "Show Method!"'

class BmwCar(Car):
  """Sub Class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
  """Sub Class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name : %s" % self.car_name

  def show(self):
    print(super().show())
    return "Car Info : %s %s %s" % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # super
print(model1.type) # super
print(model1.car_name) # sub
print(model1.show()) # super
print(model1.show_model()) # sub
print(model1.__dict__)

# Method Overriding(오버라이딩) : 동일한 이름의 부모 메소드를 변경하여 적용
model2 = BenzCar("220d", "sub", "black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", "sub", "sliver")
print(model3.show())

# Inheritance Info : 상속 정보
# 모든 클래스들은 object를 상속 받는다 즉, object가 모든 클래스들의 부모다.
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
# 너무 복잡한 다중 상속은 코드의 가독성을 저해한다.
class X():
  pass

class Y():
  pass

class Z():
  pass

class A(X, Y):
  pass

class B(Y, Z):
  pass

class M(B, A, Z) :
  pass


print(M.mro())
print(A.mro())