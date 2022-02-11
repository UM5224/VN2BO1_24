#exception_handling in python
'''
Error in Python can be of two types i.e. Syntax errors and Exceptions(logical errors)
Error in Python can be of two types i.e. Syntax errors and Exceptions(logical errors)

Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong syntax in the code.
It leads to the termination of the program

Exceptions: Exceptions are raised when the program is syntactically correct,
but the code resulted in an error.
This error does not stop the execution of the program, however, it changes the normal flow of the program

Note: Exception is the base class for all the exceptions in Python

Try and Except Statement – Catching Exceptions
Try and except statements are used to catch and handle exceptions in Python.
Statements that can raise exceptions are kept inside the try clause and the statements
that handle the exception are written inside except clause
'''
#handling single exception
try:
    print("single excepton handling with one catch bloc")
    print("exception_handling")
    print(10/0)
    print(20)
except ZeroDivisionError:
    print("zerodivision error handled")
except Exception:
    print("error not handled")

#handling multiple exception
def Error():
    try:
        print(10+b)
        print(10+"b")
    except ZeroDivisionError:
        print("zerodivision error occures and handled")
    except NameError:
        print("name error handled ")
    except ValueError:
        print("value error handled")
    else:
        print("exception is not handled")
Error()

#else clause
'''
In python, you can also use the else clause on the try-except block which must be present after all the except clauses. 
he code enters the else block only if the try clause does not raise an exception'''
def Error():
    b ="car"
    try:
        print("my"+b)
    except ZeroDivisionError:
        print("zerodivision error occures and handled")
    except TypeError:
        print("Type  error handled")
    else:
        print(" no exception in try clause")
Error()

#finally keyword
'''
Python provides a keyword finally, which is always executed after the try and except blocks. The final block always 
executes after normal termination of try block or after try block terminates due to some exception'''

def Error():
    b ="car"
    try:
        print("my"+50)
    except ZeroDivisionError:
        print("zerodivision error occures and handled")
    except TypeError:
        print("Type  error handled")
    else:
        print(" no exception in try clause")
    finally:
        print("finally keyword always execute")
Error()
# program to handle IOE error(inputoutput error)
def f():
    try:
        name = input("enter filename:   ")
        f = open(name, 'r')
    except IOError:
        print("file not found", name)
    finally:
        print("handling IOE error")
f()

# Value error
try:
    a = "hello"
    print(int(a))
except ValueError:
    print("value error handled")
finally:
    print("finish")

#index error
try:
    A =[1,2,3,4]
    print(A[20])
except IndexError:
    print("Index error handled")
finally:
    print("finish")

#assertion error
try:
    num = 43
    assert num%2==0
    print("even number")
except AssertionError:
    print("odd number")

#import error(module not found error)
try:
    from flask import Flask
except ImportError:
    print("flask module not found")