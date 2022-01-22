# class
'''
class is a combination of both state and behavior
'''
# memory allocation
'''
1)empty object will be created by python and assign it to self parameter
2)init method helps to initialise values/state of the object
'''


class Employee:

    def __init__(self,name,company,address): # Constructor
        self.name=name
        self.company=company
        self.address=address

e=Employee("jhon","abc","xyz")
#There are three different types of variables in OOPs in python.
''''
1)Instance variable ( Object level variable )
2)Static variable ( Class level variable )
3)Local variable ( Method level variable )
'''
#we can declare instance variables
'''
1)inside a constructor using self
2)inside an instance method
3)outside of class using object reference
'''
class Tree():
    def __init__(self,name,colour):#constructor
        print(self)
        self.name=name     #self.name,self.colour are instance variables
        self.colour=colour
    def grow(self):
        self.root="underground" #declare instance variable inside an instance method
        print(self.root)

t1 = Tree("neem","colour")
t1.grow()
t1.place = "india" #declare instance variable outside of class using object reference t1
print(t1.place)

'''Instance variables are created at the time of object creation and will be destroyed 
when it goes for Garbage collection'''

#We can declare static variables:
'''Inside a class but outside any method or constructor.
Inside constructor using classname.
Inside instance method using class name.
Inside class method using class name or cls variable.
Inside static method by using class name.
From outside the class by using class name.
#static variable and local variable
'''
class cal():
    subject ="maths"    #this is static variable ,which remains same for all objcts

    def __init__(self):
        self.firs_num = 50
        self.sec_num = 20

    def substraction(self,num1,num2): # here num1,num2 are local variable for this method
        sub = num2 -num1
        print(sub)


c1 = cal()
print(c1.subject)
c2 = cal()
print(c2.subject)
c1.substraction(25,100)

# different types of Methods in OOPs in python.
'''
Instance method
Static method
Class method
'''
class MyClass:
    def method(self):
        print("instance method")

    @classmethod
    def classmethod(cls):
        print("class method")

    @staticmethod
    def staticmethod():
        print("static method")

#Instance methods need a class instance and can access the instance through self
#Class methods don’t need a class instance, they can’t access the instance (self) but they have access to the class
# Static methods don’t have access to cls or self,they act as regular functions

class Cricket():
    keeper= "Dhoni" # class variable
    def __init__(self,bat,ball):# instance variables
        self.bat = bat
        self.ball = ball
    def playing(self): #instance method
        print("cricket is playing with",self.bat,"and",self.ball)
    @classmethod
    def keeping(cls):
        print(cls.keeper,"is keeping")
    @staticmethod
    def feilding():
        print("indians are feilding")

game = Cricket("mrf-bat","cork-ball")
game.playing()
game.keeping()
game.feilding()
print(game.keeper)
Cricket.captian = "Rahul"
print(Cricket.captian)


