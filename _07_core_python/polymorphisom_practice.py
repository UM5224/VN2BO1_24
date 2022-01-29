#polymorphisom-implementing the same thing in different way
'''
1)method overloading
2)method overrriding
'''
# overloading
'''
1)operator overloading
2)method overloading  #can be acheived by using default parameters
'''
#operator overloading-implementing the same operator in different way
a = 5
b = 7
print(a+b) #add two numbers
c = "good"
d = "morning"
print(c+d)# concatinating two strings

#method overloading
class One():
    def display(self,x=None,y=None,z=None): #default arguments
        print(x,y,z)
One_obj = One()
One_obj.display()
One_obj.display(10)
One_obj.display(10,20)
One_obj.display(10,20,30)
#method overriding - using inheritence
class Main():
    def view(self):
        print("Main method function")
class Child(Main):
    def view(self):
        print("Child class function")
obj1 = Main()
obj1.view()
obj2 = Child()
obj2.view()

