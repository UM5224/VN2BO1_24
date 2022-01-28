class parent():
    def func1(self):
        print("this is parent class")
class child(parent):
    def func2(self):
        print("this is child class")

ob = child()
ob.func1()
ob.func2()

class animal():
    name = "animal class"
    def speak(self):
        print("animals makes sounds")
class dog(animal):
    def bark(self):
        print("dog barks")
    def walk(self):
        print("dog has foue legs")
class cat(animal):
    a = 'cat'
d = dog()
d.speak()
print(d.name)
c = cat()
c.speak()


#encapsulation
class MainClass1():
    a=10
    b="property"
    def display(self):
        print("this is main class")


class MainClass2():
    __name="second class"
    __c =50
    def __write(self):
        print("this is second main class",self.__a)

obj = MainClass1()
obj.display()
obj2 = MainClass2()

#polymorphisom-doing same thing in differnt ways
#method overloading
#in python method overloading can be acheived with the help of default arguments
class MOverloading():
    def display(self,x=None,y=None,z=None):
        print(x,y,z)

MO = MOverloading()
MO.display()
MO.display(7365,9247)
MO.display(875,945,2387354)
#overriding
class Bus():
    def transport(self):
        print("a,b,c are on bus")
class Bike():
    def transport(self):
        print("a,b,c are on bike")
t=Bike()
t.transport()
m = Bus()
