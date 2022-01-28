#override __init__ parent method using child class
class A:
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage
    def view(self):
        print(self.name,self.age)

class B(A):
    def __init__(self,fname,fage):
        A.__init__(self,fname,fage)
        self.place = "bglr"
    def view(self):
        print(self.age,self.name,self.place)
obj = B("raj",26)
obj.view()

#overriding in ineritance
class Parent:
    def raed(self):
        print("its a function 1")

class Child():
    def read(self):
        print("its a function 2")
ob = Child()
ob.read()

