#oops
'''
python is an object oriented programming language
it uses classes and objects to develop applications and to solve problems
'''
#object
'''
object is like the real world entity
memory is allocated when the object is instanciated
we can reuse code by creating objects'''
#class
'''
class is like a blue print where properties and methods are defined
by creating objects these properties and methods can be invoked'''
#syntax
'''
class ClassName:
    #methods and properties
'''
#__init__() constructor
'''
init constructor is a special method which first run as soon as an object is created
it takes self argument and also takes other parameters'''
class MyClass:
    a = 9 # here a is class attribute

obj = MyClass()
print(obj.a)
obj.a = 0 #  setting an instance attribute
print(obj.a)
print(MyClass.a)

class Mobile():
    def __init__(self,type,colour):
        self.type=type
        self.colour=colour
    def memory(self):
        size = "16GB"
        print(size)

m = Mobile("smartphone","black")
print(m.type)
print(m.colour)
m.memory()

class Calculator():
    def __init__(self,number):
        self.number = number
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number

s = Calculator(50)
print(s.square())
print(s.cube())
