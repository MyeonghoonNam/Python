class Foo:
  def __init__(self, a, b):
    self.a = a
    self.b = b

class Bar(Foo):
  def __init__(self, **kwargs):
    super().__init__(kwargs['c'], kwargs['d'])
    self.c = kwargs['a']
    self.d = kwargs['b']

  def show(self):
    print(self.a, self.b, self.c, self.d)

Bar(a=3,b=4,c=1,d=2).show()


# def fun(*a, *b, a=a, b=b):
#   print('hi')

# fun('a','b')

def fun2(*args):
  print('hid')


a = "1"
b = "2"
c = "3"
fun2(a=40, b=20, a, b, c)