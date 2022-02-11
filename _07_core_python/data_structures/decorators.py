#decorators
'''
A decorator is a design pattern in Python that allows a user to add new functionality
to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate
'''
#assigning functions ta variables
'''
To kick us off we create a function that will add one to a number whenever it is called. 
We'll then assign the function to a variable and use this variable to call the function'''

def multip(a):
    return  a*10

m = multip
print(m(10))

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
'''
Our decorator function takes a function as an argument, and we shall, therefore, 
define a function and pass it to our decorator. 
We learned earlier that we could assign a function to a variable. 
We'll use that trick to call our decorator function'''

def ordinary():
    print("I am ordinary")
pretty = make_pretty(ordinary)
pretty()
'''
Python provides a much easier way for us to apply decorators. 
We simply use the @ symbol before the function we'd like to decorate
'''
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()




#applying multiple decotators to a single function
'''
We can use multiple decorators to a single function. However, the decorators will
be applied in the order that we've called them. 
Below we'll define another decorator that 
splits the sentence into a list. 
We'll then apply the uppercase_decorator and split_string decorator to a single function'''


def decor1(func):
    def inner():
        x = func()
        print(func())
        return x*5

    return inner


def decor(func):
    def inner():
        x = func()
        return 5 * x

    return inner
@decor1
@decor
def num():
    return 10
print(num())

'''
From the above output, we notice that the application of decorators is from the bottom up. 
Had we interchanged the order, we'd have seen an error since lists don't have an upper attribute. 
The sentence has first been converted to uppercase and then split into a list'''

#accepting arguments in decorator functions
'''
Sometimes we might need to define a decorator that accepts arguments. 
We achieve this by passing the arguments to the wrapper function. 
The arguments will then be passed to the function that is being decorated at call time'''

def decorator_one(function):
    def args(d,e):
        print("My arguments are",d,e)

    return args

@decorator_one
def name(a, b):
    print(a,b)

name("python","java")

#Defining general purpose decorators
'''
To define a general purpose decorator that can be applied to any function we use args and **kwargs.
args and **kwargs collect all positional and keyword arguments and stores them in the args and kwargs variables.
args and kwargs allow us to pass as many arguments as we would like during function calls'''


def decorator_two(function):
    def args(*args,**kwargs):
        function()
        print("My arguments are",*args,*kwargs)

    return args

@decorator_two
def name2():
    print("hello")

name2(63553,5324,87434,763,"baarath","andhra","bglr",m="some message",v=10)