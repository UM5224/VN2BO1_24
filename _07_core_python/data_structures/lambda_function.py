def my_func(x):
    return lambda a,b,c :(a*x**2) +(b*x)+c

f = my_func(300)
print(f(600,300,800))
