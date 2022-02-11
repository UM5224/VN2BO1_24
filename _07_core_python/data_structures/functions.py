#functions
'''
A function is a block of code which only runs when it is called
we can pass data as arguments
it can returrn data as a result'''
#advantages
'''
code reusability
code changes can be done only at one place'''
#types of functions
'''
builtin/predefined functions
userdefined functions'''
#defining a function
'''
def func_name():
    //block of code
'''
def wish(name):
    a="good morning "+ name
    print(a)
#calling a function
wish("jhon")

def bignumber(a,b):
    if a>b:
        print("a is bigger number")
    else:
        print("b is bigger number")

#function calling
bignumber(43,56)

#arguments and paremeters
'''
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.'''

#return types
'''
with return type
without return type'''

def multiply(a): # this function returns value
    return a*50
print(multiply(40))

def func2(): # this function doesnot return anything
    print("python functions")

func2()
# append() method doesnot return any value
#pop() method return the removed value

#function catagories
'''
1)function with parameter with return type
2)with parameters ,without return type
3)without parameters,with return type
4)without parameters,without return type'''

#passing arguments
'''
1)positional arguments 
2)default arguments
3)keyword arguments'''

def greatest(a,b,c): #positional arguments
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print("c is greater")
greatest(20,30,60)

def names(a,b,name="sam"):#default arguments
    print(a+b)
    print(name)

names(34,77)

#function to print sum of elements in a list
def sum(a):
    total = 0
    for x in list:
        total += total + x
    print(total)
list=[2,74,64,9]
sum((2,74,64,9))

#function to check if a number is in range 100
def range_in(n):
    if n in range(100):
        print("number is in range 100 ")
    else:
        print("number is not in range 100")

range_in(50)
