#연습문제 
#10.1 아무 내용도 없는 Thing 클래스를 만들어서 출력하라. 그리고 이 클래스의 example 객체를 생성해서 출력하라. 두 출력값은 같은가?
class Thing():
  pass

example = Thing()
print(example)
print(Thing)

#10.2 Thing2 클래스를 만들고, 이 클래스의 letters 속성에 값 'abc'를 할당한 후 letters를 출력하라.
class Thing2():
  letters='abc'

print(Thing2.letters)

#10.3 Thing3 클래스를 만들어라. 이번에는 인스턴스(객체)의 letters 속성에 값 'xyz'를 할당한 후 letters를 출력하라. letters를 출력하기 위해 객체를 생성해야 하는가?
class Thing3():
  def __init__(self):
    self.letters='xyz'

example=Thing3()
print(example.letters)

#10.4 name, symbol, number 인스턴스 속성을 가진 Element 클래스를 만들어라. 이 클래스로부터 'Hydrogen', 'H', 1값을 가진 객체를 생성하라.
class Element():
  def __init__(self,name,symbol,number):
    self.name=name
    self.symbol=symbol
    self.number=number
  
example= Element('Hydrogen','H',1)
print(example.name)
print(example.symbol)
print(example.number)

